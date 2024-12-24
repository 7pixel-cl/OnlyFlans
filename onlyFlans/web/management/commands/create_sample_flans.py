from django.core.management.base import BaseCommand
from web.models import Flan

class Command(BaseCommand):
    help = 'Crea flanes de ejemplo para la aplicación'

    def handle(self, *args, **kwargs):
        flanes_data = [
            {
                'name': 'Flan Clásico',
                'description': 'Nuestro flan tradicional con caramelo dorado y textura sedosa.',
                'image_url': 'https://images.unsplash.com/photo-1614707267537-b85aaf00c4b7',
                'is_private': False
            },
            {
                'name': 'Flan de Café',
                'description': 'Delicioso flan con un toque de café premium y caramelo oscuro.',
                'image_url': 'https://images.unsplash.com/photo-1587314168485-3236d6710814',
                'is_private': False
            },
            {
                'name': 'Flan de Coco',
                'description': 'Suave flan con coco rallado y leche de coco natural.',
                'image_url': 'https://images.unsplash.com/photo-1528975604071-b4dc52a2d18c',
                'is_private': False
            },
            {
                'name': 'Flan de Vainilla',
                'description': 'Flan elaborado con vainilla de Madagascar y leche cremosa.',
                'image_url': 'https://images.unsplash.com/photo-1621303837174-89787a7d4729',
                'is_private': False
            },
            {
                'name': 'Flan Premium de Chocolate',
                'description': 'Exclusivo flan de chocolate belga con cobertura de ganache.',
                'image_url': 'https://images.unsplash.com/photo-1624353365286-3f8d62daad51',
                'is_private': True
            },
            {
                'name': 'Flan Royal',
                'description': 'Flan premium con frutas exóticas y caramelo de maple.',
                'image_url': 'https://images.unsplash.com/photo-1464305795204-6f5bbfc7fb81',
                'is_private': True
            },
            {
                'name': 'Flan de Pistache VIP',
                'description': 'Flan exclusivo con pistaches tostados y crema de almendras.',
                'image_url': 'https://images.unsplash.com/photo-1515037893149-de7f840978e2',
                'is_private': True
            },
            {
                'name': 'Flan Supreme',
                'description': 'Nuestro flan más exclusivo con oro comestible y frutos rojos.',
                'image_url': 'https://images.unsplash.com/photo-1563805042-7684c019e1cb',
                'is_private': True
            }
        ]

        for flan_data in flanes_data:
            Flan.objects.create(**flan_data)
            self.stdout.write(self.style.SUCCESS(f'Flan creado: {flan_data["name"]}")) 