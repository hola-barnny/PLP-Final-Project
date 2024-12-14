import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:your_project_name/main.dart'; // import your app entry point

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  group('Mobile App Tests', () {
    testWidgets('Login and navigate to Dashboard', (WidgetTester tester) async {
      // Build the app and trigger a frame.
      await tester.pumpWidget(MyApp());

      // Find widgets
      final emailField = find.byKey(Key('email'));
      final passwordField = find.byKey(Key('password'));
      final loginButton = find.byKey(Key('login_button'));

      // Interact with widgets
      await tester.enterText(emailField, 'testuser@example.com');
      await tester.enterText(passwordField, 'password123');
      await tester.tap(loginButton);

      // Wait for the Dashboard to appear
      await tester.pumpAndSettle();

      // Verify the Dashboard text
      expect(find.text('Dashboard'), findsOneWidget);
    });

    testWidgets('Send a message', (WidgetTester tester) async {
      // Build the app and trigger a frame.
      await tester.pumpWidget(MyApp());

      // Find widgets
      final messageField = find.byKey(Key('message_input'));
      final sendButton = find.byKey(Key('send_button'));

      // Interact with widgets
      await tester.enterText(messageField, 'Hello!');
      await tester.tap(sendButton);

      // Wait for the message to be sent
      await tester.pumpAndSettle();

      // Verify the sent message text
      expect(find.text('Hello!'), findsOneWidget);
    });
  });
}
