import random
from datacenter.models import Schoolkid, Mark, Chastisement, Subject, Commendation, Lesson


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
    marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
    for mark in marks:
        mark.points = 5
        mark.save()


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

        texts = Commendation.objects.filter(subject=subject)
        comm_text = random.choice(texts).text

        Commendation.objects.create(
            text=comm_text,
            schoolkid=schoolkid,
            subject=subject,
            teacher=lesson.teacher,
            created=lesson.date
        )
    except Subject.DoesNotExist:
        print("Название предмета введено неверно или такого предмета не существует.")
