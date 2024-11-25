
/// Validate email format
bool isValidEmail(String email) {
  final emailRegExp = RegExp(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$');
  return emailRegExp.hasMatch(email);
}

/// Validate password (minimum length of 6 characters)
bool isValidPassword(String password) {
  return password.length >= 6;
}

/// Validate if a string is not empty (e.g., for required fields)
bool isNotEmpty(String value) {
  return value.isNotEmpty;
}

/// Check if a string matches a specific pattern (e.g., phone number, etc.)
bool isValidPattern(String value, RegExp pattern) {
  return pattern.hasMatch(value);
}

/// Validate phone number (example pattern)
bool isValidPhoneNumber(String phoneNumber) {
  final phoneRegExp = RegExp(r'^\+?[0-9]{10,15}$');
  return isValidPattern(phoneNumber, phoneRegExp);
}
