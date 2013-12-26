from biblebot.constants import *

__all__ = ['old_testament', 'new_testament', 'psalms', 'proverbs', 'readings']

old_testament = {}
new_testament = {}
psalms = {}
proverbs = {}

old_testament[JANUARY] = {
    1: 'Genesis 1-2:17',
    2: 'Gen 2:18-4:16',
    3: 'Gen 4:17-6:22',
    4: 'Gen 7-9:17',
    5: 'Gen 9:18-11:9',
    6: 'Gen 11:10-13',
    7: 'Gen 14-16',
    8: 'Gen 17-18',
    9: 'Gen 19:-20',
    10: 'Gen 21-23',
    11: 'Gen 24',
    12: 'Gen 25-26',
    13: 'Gen 27-28',
    14: 'Gen 29-30',
    15: 'Gen 31',
    16: 'Gen 32-33',
    17: 'Gen 34-35',
    18: 'Gen 36-37',
    19: 'Gen 38-39',
    20: 'Gen 40-41:40',
    21: 'Gen 41:41-42',
    22: 'Gen 43-44',
    23: 'Gen 45-47:12',
    24: 'Gen 47-48',
    25: 'Gen 49-50',
    26: 'Job 1-3',
    27: 'Job 4-7',
    28: 'Job 8-10',
    29: 'Job 11-14',
    30: 'Job 15-18',
    31: 'Job 19-21',
}

new_testament[JANUARY] = {
    1: 'Matthew 1',
    2: 'Mt 2:1-18',
    3: 'Mt 2:18-3:17',
    4: 'Mt 4',
    5: 'Mt 4:23-5:20',
    6: 'Mt 5:21-42',
    7: 'Mt 5:43-6:24',
    8: 'Mt 6:25-7:23',
    9: 'Mt 7:24-8:22',
    10: 'Mt 8:23-9:13',
    11: 'Mt 9:14-38',
    12: 'Mt 10:1-31',
    13: '> Mt 11:15',
    14: '> Mt 11:30',
    15: '> Mt 12:21',
    16: '> Mt 12:45',
    17: '> Mt 13:17',
    18: '> Mt 13:35',
    19: '> Mt 13:58',
    20: '> Mt 14:21',
    21: '> Mt 15:9',
    22: '> Mt 15:10-39',
    23: '> Mt 16:20',
    24: '> Mt 17:13',
    25: '> Mt 18:9',
    26: '> Mt 18:35',
    27: '> Mt 19:15',
    28: '> Mt 19:30',
    29: '> Mt 20:19',
    30: '> Mt 20:34',
    31: '> Mt 21:27',
}


psalms[JANUARY] = {
    1: 'Psalm 1',
    2: 'Ps 2',
    3: 'Ps 3',
    5: 'Ps 4',
    6: 'Ps 5',
    7: 'Ps 6',
    9: 'Ps 7',
    11: 'Ps 8',
    13: 'Ps 9',
    17: 'Ps 10',
    19: 'Ps 11',
    21: 'Ps 12',
    22: 'Ps 13',
    23: 'Ps 14',
    25: 'Ps 15',
    26: 'Ps 16',
    27: 'Ps 17',
    31: 'Ps 18',
}


proverbs[JANUARY] = {
    4: 'Prov1:1-7',
    8: 'Prov 1:8-19',
    12: 'Pr 1:20-33',
    16: 'Pr 2:1-11',
    20: 'Pr 2:12-22',
    24: 'Pr 3:1-10',
    28: 'Pr 3:11-20',
}


def _format_readings(month):
    data = {}
    for day in xrange(1, len(old_testament[month])):
        reading = [old_testament[month][day], new_testament[month][day]]
        if day in psalms[month]:
            reading.append(psalms[month][day])
        if day in proverbs[month]:
            reading.append(proverbs[month][day])
        data[day] = tuple(reading)
    return data


readings = {
    JANUARY: _format_readings(JANUARY),
    NOVEMBER: {
        1: ('Joel 1:1-2:17', 'Hebrews 3:1-19'),
        2: ('>Joel 3:21', '>Heb 4:13'),
        3: ('Ezekiel 1:1-3:27', '>Heb 5:10'),
        4: ('>Eze 6:14', '>Heb 6:12', 'Proverbs 26:23-27:4'),
        5: ('>Eze 9:11', '>Heb 7:10'),
        6: ('>Eze 12:28', '>Heb 7:28'),
        7: ('>Eze 15:8', '>Heb 8:13', 'Psalm 120'),
        8: ('>Eze 16:63', '>Heb 9:15', '>Prov 27:14'),
        9: ('>Eze 18:32', '>Heb 9:28', 'Ps 121'),
        10: ('>Eze 20:44', '>Heb 10:18', 'Ps 122'),
        11: ('>Eze 22:22', '>Heb 10:39', 'Ps 123'),
        12: ('>Eze 23:49', '>Heb 11:16', '>Prov 27:22'),
        13: ('>Eze 25:17', '>Heb 11:40', 'Ps 124'),
        14: ('>Eze 27:36', '>Heb 12:13', 'Ps 125'),
        15: ('>Eze 29:21', '>Heb 12:29', 'Ps 126'),
        16: ('>Eze 31:18', '>Heb 13:25', '>Prov 28:6'),
        17: ('>Eze 33:20', 'James 1', 'Ps 127'),
        18: ('>Eze 35:15', 'James 2', 'Ps 128'),
        19: ('>Eze 37:28', 'James 3', 'Ps 129'),
        20: ('>Eze 39:29', 'James 4', '>Prov 28:17'),
        21: ('>Eze 40:49', 'James 5', 'Ps 130'),
        22: ('>Eze 42:20', 'Ps 131'),
        23: ('>Eze 44:31', '>1 Pet 2:25', 'Ps 132'),
        24: ('>Eze 46:24', '>1 Pet 3:22', '>Prov 28:28'),
        25: ('>Eze 48:35', '>1 Pet 4:19', 'Ps 133'),
        26: ('Daniel 1:1-2:23', '>1 Pet 5:14', 'Ps 134'),
        27: ('>Dan 3:12', '2 Peter 1', 'Ps 135'),
        28: ('>Dan 4:18', '2 Peter 2', '>Prov 29:9'),
        29: ('>Dan 5:16', '2 Peter 3'),
        30: ('>Dan 6:28', '1 John 1:1-2:11', 'Ps 136'),
    },
    DECEMBER: {
        1: ('Daniel 7:1-8:14', '1 John 2:12-27'),
        2: ('>Dan 9:19', '>1 Jn 3:10', 'Proverbs 29:10-18'),
        3: ('>Dan 11:1', '>1 Jn 4:6', 'Psalm 137'),
        4: ('>Dan 11:35', '>1 Jn 4:21', 'Ps 138'),
        5: ('>Dan 12:13', '>1 Jn 5:21', 'Ps 139'),
        6: ('Haggai 1-2', '2 John 1', '>Prov 29:27'),
        7: ('Zechariah 1-4', '3 John 1'),
        8: ('Zechariah 5-8', 'Jude 1'),
        9: ('Zechariah 9-11', 'Revelation 1:1-20', 'Ps 140'),
        10: ('Zechariah 12-14', '>Rev 2:17', '>Prov 30:10'),
        11: ('Esther 1:1-2:18', '>Rev 3:6'),
        12: ('>Esther 5:14', '>Rev 3:22', 'Ps 141'),
        13: ('>Esther 8:17', '>Rev 4:11', 'Ps 142'),
        14: ('>Esther 10:3', '>Rev 5:14', '>Prov 30:23'),
        15: ('Malachi 1:1-2:16', '>Rev 6:17', 'Ps 143'),
        16: ('Malachi 2:17-4:6', '>Rev 7:17', 'Ps 144'),
        17: ('Ezra 1:1-2:67', '>Rev 9:12'),
        18: ('>Ezra 4:5', '>Rev 10:11', '>Prov 30:33'),
        19: ('>Ezra 5:17', '>Rev 11:19', 'Ps 145'),
        20: ('20 >Ezra 7:10', '>Rev 13:1a'),
        21: (' >Ezra 8:14', '>Rev 13:18'),
        22: ('>Ezra 9:15', '>Rev 14:13', '>Prov 31:9'),
        23: ('>Ezra 10:44', '>Rev 15:8', 'Ps 146'),
        24: ('Nehemiah 1:1-2:20', '>Rev 16:21', 'Ps 147'),
        25: ('>Neh 4:23', '>Rev 17:18'),
        26: ('>Neh 7:3', '>Rev 18:17a', '>Prov 31:20'),
        27: ('>Neh 8:18', '>Rev 19:10', 'Ps 148'),
        28: ('>Neh 9:37', '>Rev 19:21'),
        29: ('>Neh 11:21', '>Rev 20:15', 'Ps 149'),
        30: ('>Neh 12:47', '>Rev 21:27', '>Prov 31:31'),
        31: ('>Neh 13:31', '>Rev 22:21', 'Ps 150'),
    },
}
