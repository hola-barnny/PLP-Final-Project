import 'package:firebase_auth/firebase_auth.dart';

class AuthService {
  // Firebase login method
  static Future<String?> login(String email, String password) async {
    try {
      // Attempt to sign in with provided email and password
      await FirebaseAuth.instance.signInWithEmailAndPassword(
        email: email,
        password: password,
      );
      return null; // Login success, return null
    } catch (e) {
      // Return error message if something goes wrong
      return e.toString();
    }
  }

  // Optional: Add a logout method if needed
  static Future<void> logout() async {
    await FirebaseAuth.instance.signOut();
  }
}

