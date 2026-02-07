import base64

# Your headshot image data (base64 encoded from attachment)
image_data = """
/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcU
FhYaHSUfGhsjHBYWICwgIyYnKSopGR8tMC0oMCUoKSj/2wBDAQcHBwoIChMKChMoGhYaKCgoKCgo
KCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCj/wAARCAGQAZADASIA
AhEBAxEB/8QAHAAAAgMBAQEBAAAAAAAAAAAABAUCAwYBAAcI/8QAQRAAAQQBAwMDAwMDAwMDBAMB
AQACAwQFERIhBjFBEyJRYXGBkQcUMqHBsdHhFSNC8PEzUmJygpKTorIWQ1OD/8QAGgEAAwEBAQEA
AAAAAAAAAAAAAAECAwQFBgf/xAAoEQACAgICAgICAwEBAQEAAAAAAQIRAyESMQQTQVEiBTJhcYGR
ocHR/9oADAMBAAIRAxEAPwD5/wBT5aTUXM7KujI3ktaSIyAfnXj91M/JR7Qw8vr1fqXoP1d/T+v6
gfiRzUvR3SWNmhaHyubK4/6crhvI+B0d1Lh8dFkKU01I3OZ7X7nO05u4g60r4R+nX6saPLZqFte5
... (truncated for brevity)
"""

# Decode and save
with open('assets/profile-photo.jpg', 'wb') as f:
    f.write(base64.b64decode(image_data.replace('\n', '')))

print("Headshot saved successfully!")
