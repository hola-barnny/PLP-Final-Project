import 'package:flutter/material.dart';

class UserProvider with ChangeNotifier {
  String _userId = '';
  bool _isLoggedIn = false;

  String get userId => _userId;
  bool get isLoggedIn => _isLoggedIn;

  // Method to log in the user
  Future<void> login(String email, String password) async {
    // You can replace this logic with your actual API call
    try {
      // Simulating a successful login for testing
      if (email == 'test@example.com' && password == 'password') {
        _isLoggedIn = true;
        _userId = email;  // Storing the user ID (email in this case)
        notifyListeners();
      } else {
        throw Exception('Invalid credentials');
      }
    } catch (e) {
      throw Exception('Error during login: $e');
    }
  }

  // Logout method
  void logout() {
    _isLoggedIn = false;
    _userId = '';
    notifyListeners();
  }
}
