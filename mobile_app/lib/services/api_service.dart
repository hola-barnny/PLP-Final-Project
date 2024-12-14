import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  final String baseUrl = "https://api.classbridge.com";

  Future<dynamic> login(String email, String password) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/login'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'email': email, 'password': password}),
      );
      return jsonDecode(response.body);
    } catch (e) {
      throw Exception('Login failed: $e');
    }
  }
}
