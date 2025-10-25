import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk


class UserProfileApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("User Profile")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        self.root.configure(bg='#f8f9fa')
        self.setup_main_window()

    def setup_main_window(self):
        """Создаём метки для отображения в окне"""
        # Создаём изображения
        self.create_image_labels()

        # Основной контейнер для контента
        content_frame = tk.Frame(self.root, bg='white', relief='flat', bd=1)
        content_frame.place(x=50, y=120, width=400, height=500)

        # Имя пользователя - крупный шрифт
        user_label = tk.Label(content_frame, text="Georgii Chetverikov",
                              font=("Arial", 20, "bold"),
                              bg='white', fg='#2c3e50')
        user_label.pack(pady=(20, 10))

        # Разделительная линия
        separator1 = tk.Frame(content_frame, height=1, width=350, bg='#e9ecef')
        separator1.pack(pady=5)

        # Биография
        bio_frame = tk.Frame(content_frame, bg='white')
        bio_frame.pack(fill='x', padx=25, pady=15)

        bio_label = tk.Label(bio_frame, text="Biography",
                             font=("Arial", 14, "bold"),
                             bg='white', fg='#2c3e50', anchor='w')
        bio_label.pack(fill='x')

        about_label = tk.Label(bio_frame,
                               text="I'm a Student in MAI",
                               wraplength=350,
                               justify="left",
                               font=("Arial", 11),
                               bg='white', fg='#6c757d')
        about_label.pack(fill='x', pady=(5, 0))

        # Разделительная линия
        separator2 = tk.Frame(content_frame, height=1, width=350, bg='#e9ecef')
        separator2.pack(pady=10)

        # Умения
        skills_frame = tk.Frame(content_frame, bg='white')
        skills_frame.pack(fill='x', padx=25, pady=15)

        skills_label = tk.Label(skills_frame, text="Skills",
                                font=("Arial", 14, "bold"),
                                bg='white', fg='#2c3e50', anchor='w')
        skills_label.pack(fill='x')

        languages_label = tk.Label(skills_frame,
                                   text="Python | PHP | SQL | JavaScript",
                                   font=("Arial", 11),
                                   bg='white', fg='#6c757d')
        languages_label.pack(fill='x', pady=(8, 0))

        # Разделительная линия
        separator3 = tk.Frame(content_frame, height=1, width=350, bg='#e9ecef')
        separator3.pack(pady=10)

        # Опыт
        experience_frame = tk.Frame(content_frame, bg='white')
        experience_frame.pack(fill='x', padx=25, pady=15)

        experience_label = tk.Label(experience_frame, text="Experience",
                                    font=("Arial", 14, "bold"),
                                    bg='white', fg='#2c3e50', anchor='w')
        experience_label.pack(fill='x')

        # Python Developer
        dev_frame = tk.Frame(experience_frame, bg='white')
        dev_frame.pack(fill='x', pady=(12, 5))

        developer_label = tk.Label(dev_frame,
                                   text="Python Developer",
                                   font=("Arial", 12, "bold"),
                                   bg='white', fg='#2c3e50', anchor='w')
        developer_label.pack(fill='x')

        dev_dates_label = tk.Label(dev_frame,
                                   text="Mar 2021 - Present",
                                   font=("Arial", 10),
                                   bg='white', fg='#7f8c8d', anchor='w')
        dev_dates_label.pack(fill='x')

        # Teacher in 5-9 classes
        teacher_frame = tk.Frame(experience_frame, bg='white')
        teacher_frame.pack(fill='x', pady=(12, 5))

        teacher_label = tk.Label(teacher_frame,
                                 text="Teacher in 5-9 classes",
                                 font=("Arial", 12, "bold"),
                                 bg='white', fg='#2c3e50', anchor='w')
        teacher_label.pack(fill='x')

        teacher_dates_label = tk.Label(teacher_frame,
                                       text="Aug 2025 - ...",
                                       font=("Arial", 10),
                                       bg='white', fg='#7f8c8d', anchor='w')
        teacher_dates_label.pack(fill='x')

        # Builder
        builder_frame = tk.Frame(experience_frame, bg='white')
        builder_frame.pack(fill='x', pady=(12, 5))

        builder_label = tk.Label(builder_frame,
                                 text="Builder",
                                 font=("Arial", 12, "bold"),
                                 bg='white', fg='#2c3e50', anchor='w')
        builder_label.pack(fill='x')

        builder_dates_label = tk.Label(builder_frame,
                                       text="10.12.2024 - 15.12.2024",
                                       font=("Arial", 10),
                                       bg='white', fg='#7f8c8d', anchor='w')
        builder_dates_label.pack(fill='x')

    def create_image_labels(self):
        """Создаём метки с изображениями"""
        try:
            # Создаём синий фон программно
            bg_frame = tk.Frame(self.root, width=500, height=120, bg='#3498db')
            bg_frame.place(x=0, y=0)

            # Создаём круглый аватар
            avatar_frame = tk.Frame(self.root, width=80, height=80, bg='#3498db')
            avatar_frame.place(x=210, y=40)
            avatar_frame.pack_propagate(False)

            # Аватар с инициалами
            avatar_label = tk.Label(avatar_frame, text="GC",
                                    font=("Arial", 24, "bold"),
                                    bg='#2980b9', fg='white',
                                    relief='raised', bd=2)
            avatar_label.pack(fill='both', expand=True)

            # Попробуем загрузить изображение профиля
            try:
                profile_image = Image.open("images/profile_image.png")
                profile_image = profile_image.resize((76, 76))

                # Создаём маску для круглого изображения
                mask = Image.new('L', (76, 76), 0)
                # Здесь можно добавить создание круглой маски если нужно

                profile_photo = ImageTk.PhotoImage(profile_image)
                profile_label = tk.Label(avatar_frame, image=profile_photo, bg='#2980b9')
                profile_label.image = profile_photo
                profile_label.place(x=2, y=2, width=76, height=76)

            except Exception as e:
                print(f"Image not found, using text avatar: {e}")
                # Используем текстовый аватар, который уже создан

        except Exception as error:
            print(f"Avatar creation error: {error}")
            # Резервный вариант - простой аватар
            bg_frame = tk.Frame(self.root, width=500, height=120, bg='#3498db')
            bg_frame.place(x=0, y=0)

            avatar_label = tk.Label(self.root, text="GC",
                                    font=("Arial", 20, "bold"),
                                    bg='#2980b9', fg='white',
                                    width=4, height=2)
            avatar_label.place(x=210, y=20)

    def run(self):
        """Запуск приложения"""
        self.root.mainloop()


if __name__ == "__main__":
    app = UserProfileApp()
    app.run()