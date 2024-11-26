import 'package:flutter/material.dart';

class Constants {
  // App Title and Branding
  static const String appTitle = "Parent-Teacher Communication";
  static const String appSubtitle = "Connecting Parents and Teachers Seamlessly";

  // API Base URL (replace with your real backend API URL)
  static const String apiUrl = "http://127.0.0.1:5000";

  // Error Messages
  static const String errorNetwork = "Network error, please try again later.";
  static const String errorLogin = "Invalid email or password.";
  static const String errorUnauthorized = "You are not authorized to access this page.";
  static const String errorGeneral = "Something went wrong. Please try again.";

  // Success Messages
  static const String successLogin = "Login Successful";
  static const String successLogout = "You have been logged out.";
  static const String successDataSaved = "Data saved successfully.";
  static const String successOperation = "Operation completed successfully.";

  // Placeholder Texts
  static const String placeholderEmail = "Enter your email";
  static const String placeholderPassword = "Enter your password";
  static const String placeholderSearch = "Search...";

  // App-wide Colors
  static const Color primaryColor = Colors.blue;
  static const Color secondaryColor = Colors.blueAccent;
  static const Color errorColor = Colors.red;
  static const Color successColor = Colors.green;
  static const Color backgroundColor = Color(0xFFF5F5F5); // Light grey
  static const Color textColor = Colors.black87;

  // App-wide Text Styles
  static final TextStyle headingStyle = TextStyle(
    fontSize: 24,
    fontWeight: FontWeight.bold,
    color: textColor,
  );

  static final TextStyle subtitleStyle = TextStyle(
    fontSize: 16,
    fontWeight: FontWeight.w500,
    color: textColor,
  );

  static final TextStyle bodyTextStyle = TextStyle(
    fontSize: 14,
    color: textColor,
  );

  static final TextStyle errorTextStyle = TextStyle(
    fontSize: 14,
    color: errorColor,
  );

  static final TextStyle successTextStyle = TextStyle(
    fontSize: 14,
    color: successColor,
  );

  // App Padding and Margins
  static const double defaultPadding = 16.0;
  static const double defaultMargin = 16.0;

  // App Durations (for animations and delays)
  static const Duration animationDuration = Duration(milliseconds: 300);
  static const Duration splashScreenDelay = Duration(seconds: 3);
}
