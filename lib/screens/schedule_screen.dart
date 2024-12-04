import 'package:flutter/material.dart';
import '../services/database_service.dart';
import '../utils/constants.dart';  // Import the Constants class

class ScheduleScreen extends StatefulWidget {
  const ScheduleScreen({super.key});

  @override
  _ScheduleScreenState createState() => _ScheduleScreenState();
}

class _ScheduleScreenState extends State<ScheduleScreen> {
  final DatabaseService databaseService = DatabaseService();
  List<Map<String, String>> schedule = [];
  bool isLoading = true;

  @override
  void initState() {
    super.initState();
    fetchSchedule();
  }

  void fetchSchedule() async {
    try {
      String userId = 'user1';
      final data = await databaseService.getSchedule(userId);
      setState(() {
        schedule = data;
        isLoading = false;
      });
    } catch (e) {
      setState(() {
        isLoading = false;
      });
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Error fetching schedule: $e')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Schedule'),
      ),
      body: isLoading
          ? const Center(child: CircularProgressIndicator())
          : Padding(
              padding: EdgeInsets.all(Constants.defaultPadding),  // Use Constants for padding
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Upcoming Meetings and Events',
                    style: Constants.headingStyle,  // Use Constants for text styling
                  ),
                  const SizedBox(height: 20),
                  Expanded(
                    child: ListView.builder(
                      itemCount: schedule.length,
                      itemBuilder: (context, index) {
                        final event = schedule[index];
                        return _scheduleItem(
                          title: event['title']!,
                          date: event['date']!,
                          time: event['time']!,
                          location: event['location']!,
                        );
                      },
                    ),
                  ),
                  ElevatedButton(
                    onPressed: () {
                      ScaffoldMessenger.of(context).showSnackBar(
                        const SnackBar(content: Text('Add functionality coming soon!')),
                      );
                    },
                    child: const Text('Add New Schedule'),
                  ),
                ],
              ),
            ),
    );
  }

  Widget _scheduleItem({
    required String title,
    required String date,
    required String time,
    required String location,
  }) {
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 8.0),
      child: ListTile(
        leading: const Icon(Icons.event, color: Constants.primaryColor),  // Use Constants for icon color
        title: Text(title, style: const TextStyle(fontWeight: FontWeight.bold)),
        subtitle: Text('$date\n$time\nLocation: $location'),
        isThreeLine: true,
      ),
    );
  }
}
