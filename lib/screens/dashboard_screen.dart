import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../services/auth_provider.dart';
import '../utils/constants.dart';

class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final authProvider = Provider.of<AuthProvider>(context);

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Constants.primaryColor,
        title: Text(Constants.appTitle),
        actions: [
          IconButton(
            icon: Icon(Icons.logout),
            onPressed: () {
              authProvider.logout();
              Navigator.pushReplacementNamed(context, '/');
            },
          ),
        ],
      ),
      body: LayoutBuilder(
        builder: (context, constraints) {
          double screenWidth = constraints.maxWidth;

          return ListView(
            padding: EdgeInsets.all(Constants.defaultPadding),
            children: [
              // Student Progress Card
              GestureDetector(
                onTap: () {
                  // Navigate to the Student Progress screen
                },
                child: AnimatedContainer(
                  duration: Constants.animationDuration,
                  curve: Curves.easeInOut,
                  margin: EdgeInsets.all(Constants.defaultMargin),
                  padding: EdgeInsets.all(Constants.defaultPadding),
                  width: screenWidth,
                  height: 200,
                  decoration: BoxDecoration(
                    color: Colors.blue.shade100,
                    borderRadius: BorderRadius.circular(12),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black26,
                        blurRadius: 8,
                        offset: Offset(0, 4),
                      ),
                    ],
                  ),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(Icons.school, size: 50, color: Colors.blue),
                      SizedBox(height: 10),
                      Text(
                        'Student Progress',
                        style: Constants.headingStyle,
                      ),
                      Padding(
                        padding: const EdgeInsets.only(top: 10),
                        child: Text(
                          'View detailed performance updates and trends',
                          textAlign: TextAlign.center,
                        ),
                      ),
                    ],
                  ),
                ),
              ),

              // Messaging Card
              GestureDetector(
                onTap: () {
                  // Navigate to Messages screen
                },
                child: AnimatedContainer(
                  duration: Constants.animationDuration,
                  curve: Curves.easeInOut,
                  margin: EdgeInsets.all(Constants.defaultMargin),
                  padding: EdgeInsets.all(Constants.defaultPadding),
                  width: screenWidth,
                  height: 200,
                  decoration: BoxDecoration(
                    color: Colors.green.shade100,
                    borderRadius: BorderRadius.circular(12),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black26,
                        blurRadius: 8,
                        offset: Offset(0, 4),
                      ),
                    ],
                  ),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(Icons.message, size: 50, color: Colors.green),
                      SizedBox(height: 10),
                      Text(
                        'Messages',
                        style: Constants.headingStyle,
                      ),
                      Padding(
                        padding: const EdgeInsets.only(top: 10),
                        child: Text(
                          'Communicate with parents and teachers instantly',
                          textAlign: TextAlign.center,
                        ),
                      ),
                    ],
                  ),
                ),
              ),

              // Schedule Card
              GestureDetector(
                onTap: () {
                  // Navigate to Schedule screen
                },
                child: AnimatedContainer(
                  duration: Constants.animationDuration,
                  curve: Curves.easeInOut,
                  margin: EdgeInsets.all(Constants.defaultMargin),
                  padding: EdgeInsets.all(Constants.defaultPadding),
                  width: screenWidth,
                  height: 200,
                  decoration: BoxDecoration(
                    color: Colors.orange.shade100,
                    borderRadius: BorderRadius.circular(12),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black26,
                        blurRadius: 8,
                        offset: Offset(0, 4),
                      ),
                    ],
                  ),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(Icons.calendar_today, size: 50, color: Colors.orange),
                      SizedBox(height: 10),
                      Text(
                        'Schedule',
                        style: Constants.headingStyle,
                      ),
                      Padding(
                        padding: const EdgeInsets.only(top: 10),
                        child: Text(
                          'Manage meetings and appointments with ease',
                          textAlign: TextAlign.center,
                        ),
                      ),
                    ],
                  ),
                ),
              ),

              // Notifications Card
              GestureDetector(
                onTap: () {
                },
                child: AnimatedContainer(
                  duration: Constants.animationDuration,
                  curve: Curves.easeInOut,
                  margin: EdgeInsets.all(Constants.defaultMargin),
                  padding: EdgeInsets.all(Constants.defaultPadding),
                  width: screenWidth,
                  height: 200,
                  decoration: BoxDecoration(
                    color: Colors.purple.shade100,
                    borderRadius: BorderRadius.circular(12),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black26,
                        blurRadius: 8,
                        offset: Offset(0, 4),
                      ),
                    ],
                  ),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(Icons.notifications, size: 50, color: Colors.purple),
                      SizedBox(height: 10),
                      Text(
                        'Notifications',
                        style: Constants.headingStyle,
                      ),
                      Padding(
                        padding: const EdgeInsets.only(top: 10),
                        child: Text(
                          'Stay updated with important events and reminders',
                          textAlign: TextAlign.center,
                        ),
                      ),
                    ],
                  ),
                ),
              ),

              // Learning Resources Card
              GestureDetector(
                onTap: () {
                },
                child: AnimatedContainer(
                  duration: Constants.animationDuration,
                  curve: Curves.easeInOut,
                  margin: EdgeInsets.all(Constants.defaultMargin),
                  padding: EdgeInsets.all(Constants.defaultPadding),
                  width: screenWidth,
                  height: 200,
                  decoration: BoxDecoration(
                    color: Colors.teal.shade100,
                    borderRadius: BorderRadius.circular(12),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black26,
                        blurRadius: 8,
                        offset: Offset(0, 4),
                      ),
                    ],
                  ),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(Icons.library_books, size: 50, color: Colors.teal),
                      SizedBox(height: 10),
                      Text(
                        'Learning Resources',
                        style: Constants.headingStyle,
                      ),
                      Padding(
                        padding: const EdgeInsets.only(top: 10),
                        child: Text(
                          'Access study materials and resources shared by teachers',
                          textAlign: TextAlign.center,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          );
        },
      ),
    );
  }
}
