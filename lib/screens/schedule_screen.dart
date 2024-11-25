import 'package:flutter/material.dart';
import '../services/database_service.dart';  // Make sure to import the service

class ScheduleScreen extends StatefulWidget {
  const ScheduleScreen({Key? key}) : super(key: key);

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
    String userId = 'user1'; // Replace this with the actual user ID logic
    final data = await databaseService.getSchedule(userId); // Pass userId as argument
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
              padding: const EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text(
                    'Upcoming Meetings and Events',
                    style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
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
        leading: const Icon(Icons.event, color: Colors.blue),
        title: Text(title, style: const TextStyle(fontWeight: FontWeight.bold)),
        subtitle: Text('$date\n$time\nLocation: $location'),
        isThreeLine: true,
      ),
    );
  }
}
