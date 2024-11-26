class Message {
  final String sender;
  final String recipient;
  final String content;
  final DateTime timestamp;
  final String status;
  final String type;
  final List<String>? attachments;

  Message({
    required this.sender,
    required this.recipient,
    required this.content,
    required this.timestamp,
    this.status = "unread",
    this.type = "text",
    this.attachments,
  });

  // Factory constructor to create a Message object from JSON
  factory Message.fromJson(Map<String, dynamic> json) {
    return Message(
      sender: json['sender'],
      recipient: json['recipient'],
      content: json['content'],
      timestamp: DateTime.parse(json['timestamp']),
      status: json['status'] ?? "unread",
      type: json['type'] ?? "text",
      attachments: (json['attachments'] as List<dynamic>?)
          ?.map((attachment) => attachment as String)
          .toList(),
    );
  }

  // Method to convert Message object to JSON (useful for APIs)
  Map<String, dynamic> toJson() {
    return {
      'sender': sender,
      'recipient': recipient,
      'content': content,
      'timestamp': timestamp.toIso8601String(),
      'status': status,
      'type': type,
      'attachments': attachments,
    };
  }

  // Method to check if a message has attachments
  bool hasAttachments() => attachments != null && attachments!.isNotEmpty;
}
