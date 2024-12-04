import 'package:flutter/material.dart';

class AuthProvider extends ChangeNotifier {
  bool _isLoggedIn = false;
  String? _userEmail;

  // Getters to expose state
  bool get isLoggedIn => _isLoggedIn;
  String? get userEmail => _userEmail;

  // Login function to update authentication state
  Future<void> login(String email) async {
    _isLoggedIn = true;
    _userEmail = email;
    notifyListeners();
  }

  // Logout function to reset authentication state
  void logout() {
    _isLoggedIn = false;
    _userEmail = null;
    notifyListeners();
  }

  void checkLoginStatus() {}
}
