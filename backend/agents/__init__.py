from .base_agent import BaseAgent
from .abp_agent import ABPAgent
from .pbl_agent import PBLAgent
from .steam_agent import STEAMAgent
from .gamificacao_agent import GamificacaoAgent
from .maker_agent import MakerAgent
from .hibrido_agent import HibridoAgent
from .invertida_agent import InvertidaAgent
from .colaborativa_agent import ColaborativaAgent
from .socioemocional_agent import SocioemocionalAgent

AGENTS = {
    "abp": ABPAgent,
    "pbl": PBLAgent,
    "steam": STEAMAgent,
    "gamificacao": GamificacaoAgent,
    "maker": MakerAgent,
    "hibrido": HibridoAgent,
    "invertida": InvertidaAgent,
    "colaborativa": ColaborativaAgent,
    "socioemocional": SocioemocionalAgent,
}

__all__ = ["AGENTS", "BaseAgent"]
