from enum import Enum, IntEnum

class PerformanceFlags(Enum):
    served = 'served'
    amended = 'amended'
    saved = 'saved'
    downloaded = 'downloaded'


class ChordSymbolStructures(Enum):
    M3M7M9 = "M3M7M9"
    M3Q5M0 = "M3Q5M0"
    M3Q5M7 = "M3Q5M7"
    M3Q5M9 = "M3Q5M9"
    M3Q5O8 = "M3Q5O8"
    M3Q5m7 = "M3Q5m7"
    M3m7M9 = "M3m7M9"
    m3Q5M9 = "m3Q5M9"
    m3Q5O8 = "m3Q5O8"
    m3Q5m7 = "m3Q5m7"
    m3m7M9 = "m3m7M9"


class ChordIntervalStructures(Enum):
    M3M7M9 = [0, 4, 11, 14]
    M3Q5M0 = [0, 4, 7, 16]
    M3Q5M7 = [0, 7, 4, 11]
    M3Q5M9 = [0, 7, 4, 14]
    M3Q5O8 = [0, 12, 7, 4]
    M3Q5m7 = [0, 7, 4, 10]
    M3m7M9 = [0, 4, 10, 14]
    m3Q5M9 = [0, 7, 3, 14]
    m3Q5O8 = [0, 12, 7, 3]
    m3Q5m7 = [0, 7, 3, 10]
    m3m7M9 = [0, 3, 10, 14]


class GraphNames(Enum):
    major_graph = "major_graph"
    minor_graph = "minor_graph"
    mixed_graph = "mixed_graph"
    master_graph = "master_graph"
    default_graph = "default_graph"


class NotesInt(IntEnum):
    C = 0
    C_SHARP = 1
    D = 2
    D_SHARP = 3
    E = 4
    F = 5
    F_SHARP = 6
    G = 7
    G_SHARP = 8
    A = 9
    A_SHARP = 10
    B = 11

class NotesSymbol(Enum):
    C = 'C'
    C_SHARP = 'C#'
    D = 'D'
    D_SHARP = 'D#'
    E = 'E'
    F = 'F'
    F_SHARP = 'F#'
    G = 'G'
    G_SHARP = 'G#'
    A = 'A'
    A_SHARP = 'A#'
    B = 'B'


class NodeIDs(Enum):
    NORM1_MAJ = "NORM1+"
    NORM1_MIN = "NORM1-"
    FLAT2_MAJ = "FLAT2+"
    SHRP2_MIN = "SHRP2-"
    FLAT3_MAJ = "FLAT3+"
    SHRP3_MIN = "SHRP3-"
    NORM4_MAJ = "NORM4+"
    NORM4_MIN = "NORM4-"
    NORM5_MAJ = "NORM5+"
    NORM5_MIN = "NORM5-"
    FLAT6_MAJ = "FLAT6+"
    SHRP6_MIN = "SHRP6-"
    FLAT7_MAJ = "FLAT7+"
    SHRP7_MIN = "SHRP7-"

class NodeBase(IntEnum):
    NORM1_MAJ = 0
    NORM1_MIN = 0
    FLAT2_MAJ = 1
    SHRP2_MIN = 2
    FLAT3_MAJ = 3
    SHRP3_MIN = 4
    NORM4_MAJ = 5
    NORM4_MIN = 5
    NORM5_MAJ = 7
    NORM5_MIN = 7
    FLAT6_MAJ = 8
    SHRP6_MIN = 9
    FLAT7_MAJ = 10
    SHRP7_MIN = 11

class ChordTypes(Enum):
    MAJ = '+'
    MIN = '-'
    DIM = 'd'
    AUG = 'a'
    SUS = 's'

class StructureSymbols(Enum):
    octave = "8"
    nineth = "9"
    seventh = "7"
    third = "0"

class StructureValues(Enum):
    octave = None
    nineth = 9
    seventh = 7
    third = None

