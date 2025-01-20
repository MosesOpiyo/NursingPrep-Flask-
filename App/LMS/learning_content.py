from flask import Flask, jsonify, request
import requests


config = {
    "name": "Naxlex Library Collection",
    "url": "https://account.naxlex.com/",
    "question_url": "https://account.naxlex.com/livewire/message/question-component",
    "headers": {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://account.naxlex.com/",
        "Connection": "keep-alive",
        "Cookie": "_ga_JH8Y4MPXMK=GS1.1.1734598441.1.1.1734599693.0.0.0; _ga=GA1.1.1934935722.1734598441; _hjSessionUser_3838312=eyJpZCI6IjRmNGE0M2ZiLWI4NjUtNTA1NC05NjU0LTQ5ZDMzOGJjMzZmNiIsImNyZWF0ZWQiOjE3MzQ1OTg0NDYyNDQsImV4aXN0aW5nIjp0cnVlfQ==; twk_uuid_6441802231ebfa0fe7f98126=%7B%22uuid%22%3A%221.1hHRBBWMKzB4ekjye2zbZpxQszbwUE1J6S9cJhaozPYuk82dzqJfTBus38GNZ9nihAltzEL4fWnGgT1xV3kQ2Cz99SVyzSfCvHf2x2U9fkMlfPDn8Oo%22%2C%22version%22%3A3%2C%22domain%22%3A%22naxlex.com%22%2C%22ts%22%3A1734604722992%7D; XSRF-TOKEN=eyJpdiI6IktqM3pCK1JqQlVUcTRHeWVabTFia0E9PSIsInZhbHVlIjoibllocUhCbitxVW9sVDJsdVdkSkdmeUQ1b2N4Si9ZZjl6RmUyUXZiL0VCb3QwZ1lyZGIzbGRwL0xUQTB0TUZLdFdodW9xZ1E0QUE0WnhIcm5COE9aQ0Z3dkZ4SUlVZ2kxeERpZ0c3L3hEd0FXNkZwRytFc1pMRUdrU3B0TytEYW4iLCJtYWMiOiI3MTFmNDhiNWQ2ODRkYWJiZTU1ZTIyYWRjNTA5M2RmZDljNmUxM2M1ZmIzZDMyMWM3NzlkZjljNDUwN2ZhNTFiIn0%3D; naxlex_session=eyJpdiI6InFqNkxDd1NZbW5XRlI0ZVk3M1p6OUE9PSIsInZhbHVlIjoiemIrcUFRd1hiOEMzV0NiR1pYNnVUVDBxVTJLckNEd3gySGhtK2xTSUdmcjd4Z2NiSFpPaHVGRHR0ZFc5Q1NMMXU2RXVGZ1RPZnlVRWRMaEN5RGI5cHN5aUk2YnJuVEllNTI3T0ZXN080SitsbUY2SzhXZUVLWmY1S3daRjRnbjYiLCJtYWMiOiIxM2FmMjNkNmFkMmNhZWUzZmUxN2FjMzE0YWM2YTMzYTE4NjBlYzI0OWRkNTk4NjNhYzM0Nzc1YTNjMDdjMzIwIn0%3D",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "iframe",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Priority": "u=4",
        "TE": "trailers",
        "Origin": "https://account.naxlex.com",
        "X-CSRF-TOKEN": "OLDYewozhNRAYAB7CpmFHYOL26y0eX8EBwX1XjhW",
        "X-Livewire": "true",
        "X-Socket-ID": "undefined"
    },
    "course_base_url": "https://account.naxlex.com/client/video-stream/percent-and-decimals"
}

def get_course(course):
    try:
        course_url = f"{config['course_base_url']}"

        # Send a POST request to the Naxlex question URL
        response = requests.get(
            course_url,
            headers=config["headers"],
        )

        # Return the response from Naxlex API
        return jsonify({
            "status_code": response.status_code,
            "data": response.json() if response.headers.get('Content-Type') == 'application/json' else response.text
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500