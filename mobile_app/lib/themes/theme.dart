import 'package:flutter/material.dart';

class AppTheme {
  static const Color primaryColor = Color(0xFFFB8C00); // Orange
  static const Color secondaryColor = Color(0xFF4CAF50); // Mint Green
  static const Color textColor = Color(0xFF212121); // Dark Gray
  static const Color accentColor = Color(0xFFFFF176); // Light Yellow

  static final ThemeData lightTheme = ThemeData(
    primaryColor: primaryColor,
    colorScheme: ColorScheme.light(
      primary: primaryColor,
      secondary: accentColor,
      background: Colors.white,
    ),
    scaffoldBackgroundColor: Colors.white,
    appBarTheme: const AppBarTheme(
      backgroundColor: primaryColor,
      iconTheme: IconThemeData(color: Colors.white),
    ),
    buttonTheme: ButtonThemeData(
      buttonColor: primaryColor,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(12), // Remove `const` here
      ),
    ),
    // Updated textTheme parameters
    textTheme: const TextTheme(
      bodyLarge: TextStyle(color: textColor),
      bodyMedium: TextStyle(color: textColor),
      bodySmall: TextStyle(color: textColor),
    ),
  );

  static final ThemeData darkTheme = ThemeData(
    primaryColor: primaryColor,
    colorScheme: ColorScheme.dark(
      primary: primaryColor,
      secondary: accentColor,
      background: Colors.black,
    ),
    scaffoldBackgroundColor: Colors.black,
    appBarTheme: const AppBarTheme(
      backgroundColor: primaryColor,
      iconTheme: IconThemeData(color: Colors.white),
    ),
    buttonTheme: ButtonThemeData(
      buttonColor: primaryColor,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(12),
      ),
    ),
    // Updated textTheme parameters
    textTheme: const TextTheme(
      bodyLarge: TextStyle(color: Colors.white),
      bodyMedium: TextStyle(color: Colors.white),
      bodySmall: TextStyle(color: Colors.white),
    ),
  );
}
