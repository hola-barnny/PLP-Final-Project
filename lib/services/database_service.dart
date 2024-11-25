import 'package:http/http.dart' as http;
import 'dart:convert';

class DatabaseService {
  final String _baseUrl = 'http://127.0.0.1:5000'; // Replace with your backend URL

  // Login user
  Future<Map<String, dynamic>> loginUser(String email, String password) async {
    try {
      final response = await http.post(
        Uri.parse('$_baseUrl/login'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'email': email, 'password': password}),
      );
      if (response.statusCode == 200) {
        return jsonDecode(response.body);
      } else {
        throw Exception('Failed to log in: ${response.body}');
      }
    } catch (e) {
      throw Exception('Error logging in: $e');
    }
  }

  // Fetch student progress
  Future<List<dynamic>> getStudentProgress(String studentId) async {
    try {
      final response = await http.get(
        Uri.parse('$_baseUrl/progress/$studentId'),
      );
      if (response.statusCode == 200) {
        return jsonDecode(response.body);
      } else {
        throw Exception('Failed to fetch progress: ${response.body}');
      }
    } catch (e) {
      throw Exception('Error fetching progress: $e');
    }
  }

  // Fetch messages
  Future<List<dynamic>> getMessages(String senderId, String recipientId) async {
  try {
    final response = await http.get(
      Uri.parse('$_baseUrl/messages?sender=$senderId&recipient=$recipientId'),
    );
    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception('Failed to fetch messages: ${response.body}');
    }
  } catch (e) {
    throw Exception('Error fetching messages: $e');
  }
}


  // Post a new message
  Future<bool> sendMessage(String senderId, String recipientId, String message) async {
    try {
      final response = await http.post(
        Uri.parse('$_baseUrl/messages'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'senderId': senderId,
          'recipientId': recipientId,
          'message': message,
        }),
      );
      return response.statusCode == 201;
    } catch (e) {
      throw Exception('Error sending message: $e');
    }
  }

  // Fetch schedule
  Future<List<Map<String, String>>> getSchedule(String userId) async {
    try {
      final response = await http.get(
        Uri.parse('$_baseUrl/schedule/$userId'),
      );
      if (response.statusCode == 200) {
        return List<Map<String, String>>.from(jsonDecode(response.body));
      } else {
        throw Exception('Failed to fetch schedule: ${response.body}');
      }
    } catch (e) {
      throw Exception('Error fetching schedule: $e');
    }
  }

  // Mock function for fetching schedule data (useful for testing without a backend)
  Future<List<Map<String, String>>> getMockSchedule() async {
    await Future.delayed(const Duration(seconds: 2)); // Simulate network delay
    return [
      {'title': 'Parent-Teacher Meeting', 'date': 'Nov 28, 2024', 'time': '10:00 AM - 11:00 AM', 'location': 'Room A101'},
      {'title': 'Science Fair Preparation', 'date': 'Dec 5, 2024', 'time': '2:00 PM - 3:30 PM', 'location': 'School Auditorium'},
      {'title': 'Progress Report Discussion', 'date': 'Dec 10, 2024', 'time': '1:00 PM - 2:00 PM', 'location': 'Room B202'},
    ];
  }

  // Update schedule
  Future<bool> updateSchedule(String scheduleId, Map<String, dynamic> updates) async {
    try {
      final response = await http.put(
        Uri.parse('$_baseUrl/schedule/$scheduleId'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode(updates),
      );
      return response.statusCode == 200;
    } catch (e) {
      throw Exception('Error updating schedule: $e');
    }
  }
}
