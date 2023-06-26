import random
from datacenter.models import Schoolkid, Mark, Chastisement, Subject, Commendation, Lesson

TEXTS = ["Молодец!", "Отлично!", "Хорошо!", "Гораздо лучше, чем я ожидал!", 
        "Ты меня приятно удивил!", "Великолепно!", "Прекрасно!", 
        "Ты меня очень обрадовал!", "Именно этого я давно ждал от тебя!", 
        "Сказано здорово – просто и ясно!", "Ты, как всегда, точен!", 
        "Очень хороший ответ!", "Талантливо!", "Ты сегодня прыгнул выше головы!", 
        "Я поражен!", "Уже существенно лучше!", "Потрясающе!", "Замечательно!", 
        "Прекрасное начало!", "Так держать!", "Ты на верном пути!", "Здорово!", 
        "Это как раз то, что нужно!", "Я тобой горжусь!", 
        "С каждым разом у тебя получается всё лучше!", "Мы с тобой не зря поработали!", 
        "Я вижу, как ты стараешься!", "Ты растешь над собой!", "Ты многое сделал, я это вижу!", 
        "Теперь у тебя точно все получится!"]


def select_schoolkid(schoolkid_name: str):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        print(f"Выбран ученик {schoolkid.year_of_study}{schoolkid.group_letter} класса {schoolkid.full_name}.")
        return schoolkid
    except Schoolkid.DoesNotExist:
        print("Такого ученика не существует, либо ФИО указано неверно.")
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько учеников с похожим именем. Уточните ФИО.")


def fix_marks(schoolkid: Schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4).update(points=5)


def remove_chastisements(schoolkid: Schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(schoolkid: Schoolkid, subject_title: str):
    try:
        subject = Subject.objects.get(title=subject_title.title(), year_of_study=schoolkid.year_of_study)
        lessons = Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,

        )
        if not lessons:
            raise Lesson.EmptyResultSet
        
        # Поиск урока без похвалы
        lesson = random.choice(lessons)
        while True:
            try:
                Commendation.objects.get(
                    schoolkid=schoolkid,
                    created=lesson.date,
                    subject=subject)
                lesson = random.choice(lessons)
            except Commendation.DoesNotExist:
                break

        comm_text = random.choice(TEXTS)
        Commendation.objects.create(
            text=comm_text,
            schoolkid=schoolkid,
            subject=subject,
            teacher=lesson.teacher,
            created=lesson.date
        )
    except Subject.DoesNotExist:
        print("Название предмета введено неверно или такого предмета не существует.")
    except Lesson.EmptyResultSet:
        print("Не найдено уроков для выбранного ученика или его класса.")
