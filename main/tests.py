from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from main.models import Experience, Project

class MainAppTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Open House Fasilkom 2026",
            description="Person in Contact of Digital Engagement and Collaboration",
            category="volunteer",
            thumbnail="/static/img/experience/logoOH26.png"
        )
        
        self.project = Project.objects.create(
            nama="iMaba",
            tipe="web",
            deskripsi="Mengerjakan bagian sistem di fasilkom, navigasi informasi non akademik, denah fasilkom dan ngoding101.",
            thumbnail="/static/img/project/iMaba.png",
            link="https://bem.cs.ui.ac.id/imaba",
            skillset="Next.js, TypeScript"
        )

    def test_general_urls_are_accessible_and_use_correct_templates(self):
        response = self.client.get(reverse("main:show_menu"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu.html")

        response = self.client.get(reverse("main:show_about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")

        response = self.client.get(reverse("main:show_contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")

        response = self.client.get(reverse("main:show_artfolio"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "artfolio.html")
        self.assertContains(response, "Belum akan di implement di versi 0.2.x")

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-ngasal-yang-nggak-ada/")
        self.assertEqual(response.status_code, 404)

    def test_experience_page_shows_data(self):
        response = self.client.get(reverse("main:show_experience"))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Volunteer")
        self.assertContains(response, "Now")

    def test_project_page_shows_data(self):
        response = self.client.get(reverse("main:show_project"))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html") 
        self.assertContains(response, self.project.nama)
        self.assertContains(response, "Web Development")
        self.assertContains(response, "Next.js, TypeScript")
        self.assertContains(response, self.project.link)

    def test_experience_page_empty_state(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_project_page_empty_state(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:show_project"))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada project yang ditambahkan.")

    def test_experience_is_ongoing_property(self):
        self.assertTrue(self.experience.is_ongoing)
        
        self.experience.ended_at = timezone.now()
        self.experience.save()
        self.assertFalse(self.experience.is_ongoing)