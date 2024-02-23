from django.test import TestCase
from django.utils import timezone
from base.models import AdminNotice

class AdminNoticeModelTest(TestCase):
    def test_admin_notice_creation(self):
        """
        Test case to ensure the creation and behavior of the AdminNotice model.

        This test creates a sample AdminNotice instance, checks the __str__ method,
        and verifies if the fields were saved correctly. It also ensures that the
        date_sent is not in the future.
        """
        # Create a sample AdminNotice instance
        notice = AdminNotice.objects.create(
            sender="Admin",
            receiver="JohnDoe",
            subject="Test Subject",
            body="Test Body",
            date_sent=timezone.now()
        )

        # Check if the __str__ method returns the expected string
        self.assertEqual(str(notice), "Test Subject")

        # Check if the fields were saved correctly
        self.assertEqual(notice.sender, "Admin")
        self.assertEqual(notice.receiver, "JohnDoe")
        self.assertEqual(notice.subject, "Test Subject")
        self.assertEqual(notice.body, "Test Body")

        # Check if the date_sent is not in the future
        self.assertLessEqual(notice.date_sent, timezone.now())
