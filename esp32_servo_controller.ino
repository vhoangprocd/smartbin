/*
 * CODE ARDUINO CHO ESP32
 * Điều khiển Servo Motor dựa trên lệnh từ Python
 * 
 * Cài đặt phần cứng:
 * - Servo Signal → GPIO 23 (có thể đổi)
 * - Servo GND → GND ESP32
 * - Servo VCC → 5V ESP32
 * 
 * Thư viện cần: ESP32Servo (cài qua Arduino IDE)
 * 
 * Cách nạp:
 * 1. Cài Arduino IDE
 * 2. Board: ESP32 Dev Module
 * 3. Port: COM3 (hoặc cổng của bạn)
 * 4. Speed: 115200
 * 5. Click Upload
 */

#include <ESP32Servo.h>
#include <ArduinoJson.h>

// ===== CẤUHÌNH =====
#define SERVO_PIN 23           // GPIO pin cho servo
#define SERIAL_BAUD 115200     // Baud rate Serial
#define CENTER_ANGLE 90        // Góc trung tâm
#define LEFT_ANGLE 0           // Góc xoay trái (0°)
#define RIGHT_ANGLE 180        // Góc xoay phải (180°)

// ===== BIẾN TOÀN CỤC =====
Servo myServo;
int currentAngle = CENTER_ANGLE;
const int BUFFER_SIZE = 256;
char jsonBuffer[BUFFER_SIZE];
int bufferIndex = 0;

// ===== SETUP =====
void setup() {
  // Khởi tạo Serial
  Serial.begin(SERIAL_BAUD);
  delay(2000);
  
  Serial.println("\n\n================================");
  Serial.println("🤖 ESP32 Servo Controller v1.0");
  Serial.println("================================");
  Serial.println("✅ Khởi tạo thành công!");
  Serial.print("📡 Baud Rate: ");
  Serial.println(SERIAL_BAUD);
  Serial.print("🎯 Servo Pin: GPIO");
  Serial.println(SERVO_PIN);
  Serial.println("================================\n");
  
  // Khởi tạo servo
  myServo.attach(SERVO_PIN);
  centerServo();  // Đưa servo về trung tâm
  
  Serial.println("Sẵn sàng nhận lệnh JSON từ Python...\n");
}

// ===== LOOP CHÍNH =====
void loop() {
  // Đọc dữ liệu từ Serial
  while (Serial.available() > 0) {
    char ch = Serial.read();
    
    // Nếu gặp newline, xử lý lệnh
    if (ch == '\n') {
      jsonBuffer[bufferIndex] = '\0';
      processCommand(jsonBuffer);
      bufferIndex = 0;
    } else if (ch != '\r') {
      // Thêm ký tự vào buffer
      if (bufferIndex < BUFFER_SIZE - 1) {
        jsonBuffer[bufferIndex++] = ch;
      }
    }
  }
  
  delay(10);
}

// ===== XỬ LÝ LỆNH JSON =====
void processCommand(const char* jsonStr) {
  Serial.print("📥 Lệnh nhận: ");
  Serial.println(jsonStr);
  
  // Parse JSON
  StaticJsonDocument<256> doc;
  DeserializationError error = deserializeJson(doc, jsonStr);
  
  if (error) {
    Serial.print("❌ Lỗi JSON: ");
    Serial.println(error.c_str());
    Serial.println("{\"status\": \"error\", \"message\": \"JSON parse failed\"}");
    return;
  }
  
  // Lấy action
  const char* action = doc["action"] | "unknown";
  
  Serial.print("🔄 Action: ");
  Serial.println(action);
  
  // Xử lý các lệnh khác nhau
  if (strcmp(action, "rotate") == 0) {
    handleRotate(doc);
  } 
  else if (strcmp(action, "center") == 0) {
    centerServo();
    sendResponse("ok", "Servo centered");
  } 
  else if (strcmp(action, "stop") == 0) {
    stopServo();
    sendResponse("ok", "Servo stopped");
  }
  else if (strcmp(action, "status") == 0) {
    char msg[64];
    sprintf(msg, "Current angle: %d", currentAngle);
    sendResponse("ok", msg);
  }
  else {
    sendResponse("error", "Unknown action");
  }
}

// ===== XỬ LÝ LỆNH XOAY =====
void handleRotate(JsonDocument& doc) {
  int angle = doc["angle"] | CENTER_ANGLE;
  const char* direction = doc["direction"] | "center";
  int speed = doc["speed"] | 50;
  
  // Giới hạn angle 0-180
  angle = constrain(angle, 0, 180);
  
  Serial.print("📍 Angle: ");
  Serial.print(angle);
  Serial.print("° | Direction: ");
  Serial.print(direction);
  Serial.print(" | Speed: ");
  Serial.println(speed);
  
  rotateServo(angle, speed);
  
  char msg[64];
  sprintf(msg, "Rotated to %d degrees (%s)", angle, direction);
  sendResponse("ok", msg);
}

// ===== HÀM XỐY SERVO =====
void rotateServo(int targetAngle, int speed) {
  int step = (speed > 0) ? 1 : -1;
  int delay_ms = map(abs(speed), 0, 255, 50, 2);
  
  Serial.print("🔄 Xoay từ ");
  Serial.print(currentAngle);
  Serial.print("° đến ");
  Serial.print(targetAngle);
  Serial.println("°...");
  
  // Xoay từng bậc
  while (currentAngle != targetAngle) {
    currentAngle += step;
    currentAngle = constrain(currentAngle, 0, 180);
    
    myServo.write(currentAngle);
    delay(delay_ms);
    
    // Debug mỗi 10 bậc
    if (currentAngle % 10 == 0) {
      Serial.print("  ");
      Serial.print(currentAngle);
      Serial.println("°");
    }
  }
  
  Serial.print("✅ Đã đạt góc ");
  Serial.print(currentAngle);
  Serial.println("°");
}

// ===== ĐƯA SERVO VỀ TRUNG TÂM =====
void centerServo() {
  Serial.println("📍 Đưa servo về trung tâm (90°)...");
  rotateServo(CENTER_ANGLE, 100);
  sendResponse("ok", "Centered to 90 degrees");
}

// ===== DỪNG SERVO =====
void stopServo() {
  Serial.println("⏹️ Dừng servo");
  myServo.detach();
  delay(1000);
  myServo.attach(SERVO_PIN);
  sendResponse("ok", "Servo stopped");
}

// ===== GỬI PHẢN HỒI =====
void sendResponse(const char* status, const char* message) {
  StaticJsonDocument<256> response;
  response["status"] = status;
  response["message"] = message;
  response["angle"] = currentAngle;
  response["timestamp"] = millis();
  
  serializeJson(response, Serial);
  Serial.println();
}

// ===== HÀM DEBUG =====
void debugPrintAngle() {
  Serial.print("📍 Current angle: ");
  Serial.print(currentAngle);
  Serial.println("°");
}

/*
 * ===== LỆNH JSON CÓ THỂ GỬI TỪ PYTHON =====
 * 
 * 1. Xoay servo sang trái:
 *    {"action": "rotate", "angle": 0, "speed": 50, "direction": "left"}
 * 
 * 2. Xoay servo sang phải:
 *    {"action": "rotate", "angle": 180, "speed": 50, "direction": "right"}
 * 
 * 3. Đưa về trung tâm:
 *    {"action": "center", "angle": 90}
 * 
 * 4. Dừng servo:
 *    {"action": "stop"}
 * 
 * 5. Checking trạng thái:
 *    {"action": "status"}
 */
