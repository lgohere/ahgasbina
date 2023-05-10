from ..models import Chamada


def add_chamada(new_chamada):
    chamada = Chamada(description=new_chamada)
    chamada.save()
    return chamada.to_dict_json()


def list_chamadas():
    chamadas = Chamada.objects.all()
    return [item.to_dict_json() for item in chamadas]
