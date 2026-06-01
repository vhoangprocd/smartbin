#!/usr/bin/env python3
"""Push repository helper (cross-platform)
Usage:
  python push_repo.py --remote https://github.com/owner/repo.git --name "Your Name" --email you@example.com

If --remote is omitted, the script will use existing origin.
"""
import argparse
import subprocess
import sys
import os


def run(cmd, check=True):
    print('> ' + ' '.join(cmd))
    res = subprocess.run(cmd, cwd=os.getcwd())
    if check and res.returncode != 0:
        raise SystemExit(res.returncode)


def has_commits():
    try:
        subprocess.run(['git','rev-parse','--verify','HEAD'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--remote', '-r', help='remote URL to set as origin')
    parser.add_argument('--name', help='git user.name to set locally')
    parser.add_argument('--email', help='git user.email to set locally')
    parser.add_argument('--global', dest='global_cfg', action='store_true', help='set git config globally')
    parser.add_argument('--message', '-m', default='Initial commit', help='commit message for initial commit')
    args = parser.parse_args()

    # ensure git exists
    try:
        subprocess.run(['git','--version'], check=True, stdout=subprocess.DEVNULL)
    except Exception:
        print('ERROR: git not found in PATH')
        sys.exit(1)

    # set identity
    if args.name:
        cfg_scope = '--global' if args.global_cfg else '--local'
        run(['git','config', cfg_scope, 'user.name', args.name])
    if args.email:
        cfg_scope = '--global' if args.global_cfg else '--local'
        run(['git','config', cfg_scope, 'user.email', args.email])

    # set remote
    if args.remote:
        # remove existing origin if present
        try:
            subprocess.run(['git','remote','remove','origin'], check=False)
        except Exception:
            pass
        run(['git','remote','add','origin', args.remote])

    # create initial commit if none
    if not has_commits():
        print('No commits found. Creating initial commit...')
        run(['git','add','.'])
        run(['git','commit','-m', args.message])
    else:
        print('Repository already has commits.')

    # ensure branch main
    run(['git','branch','-M','main'], check=False)

    # push
    print('Pushing to origin main...')
    try:
        run(['git','push','-u','origin','main'])
    except SystemExit as e:
        print('Push failed. Check remote URL and credentials.')
        raise

    print('✅ Push completed.')

if __name__ == '__main__':
    main()
