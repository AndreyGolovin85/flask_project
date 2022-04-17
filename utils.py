import json


def load_candidates() -> list:
    """
    Функция загружает json файл
    :return: list
    """
    with open("json/candidates.json", "r", encoding="utf8") as file:
        return json.load(file)


def candidats_formats(list) -> str:
    """
    Функция возвращает форматированый список кандидатов ввиде строки
    :param list: list
    :return: str
    """
    candidat_format = ""
    for candidat in list:
        candidat_format += (
            "<pre>"
            f"Имя кандидата - {candidat['name']}\n"
            f"Позиция кандидата - {candidat['position']}\n"
            f"Навыки через запятую - {candidat['skills']}\n"
            "</pre>"
        )
    return candidat_format


def candidat_id(id) -> dict:
    """
    Функция находит кандидата по id
    :param id: int
    :return: dict
    """
    for candidat in load_candidates():
        if candidat["id"] == id:
            return candidat


def candidat_skills(skill) -> list:
    """
    функция отбирает кондидатов по навыку skill
    :param skill: str
    :return: list
    """
    list_candidat = []
    for candidat in load_candidates():
        skill_list = candidat["skills"].lower().split(", ")
        if skill.lower() in skill_list:
            list_candidat.append(candidat)

    return list_candidat
