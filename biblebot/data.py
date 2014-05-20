import sys

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
    9: 'Gen 19-20',
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

old_testament[FEBRUARY] = {
    1: 'Job 22-24',
    2: 'Job 25-29',
    3: 'Job 30-32',
    4: 'Job 33-34',
    5: 'Job 35-37',
    6: 'Job 38:40:2',
    7: 'Job 40-42',
    8: 'Exodus 1-3',
    9: 'Ex 4-6:12',
    10: 'Ex 6:13-8',
    11: 'Ex 9-10',
    12: 'Ex 11-12',
    13: 'Ex 13-14',
    14: 'Ex 15-16',
    15: 'Ex 17-18',
    16: 'Ex 19-20',
    17: 'Ex 21-22',
    18: 'Ex 23-24:18',
    19: 'Ex 25-26',
    20: 'Ex 27-28',
    21: 'Ex 29-30',
    22: 'Ex 31-33:6',
    23: 'Ex 33-34',
    24: 'Ex 35-36',
    25: 'Ex 37-38',
    26: 'Ex 39-40',
    27: 'Leviticus 1-3',
    28: 'Lev 4-5:13',
}

new_testament[FEBRUARY] = {
    1: 'Matthew 21:28-21:32',
    2: '> Mt 22:14',
    3: '> Mt 22:46',
    4: '> Mt 23:19',
    5: '> Mt 24:31',
    6: '> Mt 25:13',
    7: '> Mt 25:46',
    8: '> Mt 26:30',
    9: '> Mt 26:46',
    10: '> Mt 26:68',
    11: '> Mt 27:10',
    12: '> Mt 27:44',
    13: '> Mt 27:66',
    14: 'Mt 28',
    15: 'Mark 1:1-28',
    16: '> Mk 2:17',
    17: '> Mk 3:30',
    18: '> Mk 4:29',
    19: '> Mk 5:20',
    20: '> Mk 6:6a',
    21: '> Mk 6:29',
    22: '> Mk 6:56',
    23: '> Mk 7:30',
    24: '> Mk 8:13',
    25: '> Mk 9:1',
    26: '> Mk 9:32',
    27: '> Mk 10:12',
    28: '> Mk 10:31',
}

psalms[FEBRUARY] = {
    8: 'Ps 19',
    11: 'Ps 20',
    12: 'Ps 21',
    15: 'Ps 22',
    19: 'Ps 23',
    20: 'Ps 24',
    22: 'Ps 25',
    26: 'Ps 26',
    27: 'Ps 27',
}

proverbs[FEBRUARY] = {
    1: 'Prove 3:21-35',
    5: 'Pr 4:1-9',
    9: 'Pr 4:10-19',
    13: 'Pr 4:20-27',
    17: 'Pr 5:1-14',
    21: 'Pr 5:15-23',
    25: 'Pr 6:1-11',
}

old_testament[MARCH] = {
    1: 'Lev 5:14-7:10',
    2: '>Lev 8:36',
    3: '>Lev 10:20',
    4: '>Lev 12:8',
    5: '>Lev 13:59',
    6: '>Lev 14:57',
    7: '>Lev 16:34',
    8: '>Lev 18:30',
    9: '>Lev 20:27',
    10: '>Lev 22:33',
    11: '>Lev 24:23',
    12: '>Lev 26:13',
    13: '>Lev 27:34',
    14: 'Num 1:1-2:9',
    15: '>Num 3:51',
    16: '>Num 5:10',
    17: '>Num 6:27',
    18: '>Num 7:65',
    19: '>Num 9:14',
    20: '>Num 11:3',
    21: '>Num 13:25',
    22: '>Num 14:45',
    23: '>Num 16:35',
    24: '>Num 18:32',
    25: '>Num 21:3',
    26: '>Num 22:20',
    27: '>Num 23:26',
    28: '>Num 26:11',
    29: '>Num 27:11',
    30: '>Num 29:11',
    31: '>Num 31:24',
}

new_testament[MARCH] = {
    1: 'Mk 10:32-52',
    2: '>Mk 11:25',
    3: '>Mk 12:12',
    4: '>Mk 12:27',
    5: '>Mk 12:44',
    6: '>Mk 13:31',
    7: '>Mk 14:16',
    8: '>Mk 14:42',
    9: '>Mk 14:72',
    10: '>Mk 15:32',
    11: '>Mk 15:47',
    12: '>Mk 16:20',
    13: 'Lk 1:1-25',
    14: '>Lk 1:38',
    15: '>Lk 1:56',
    16: '>Lk 1:80',
    17: '>Lk 2:20',
    18: '>Lk 2:40',
    19: '>Lk 2:52',
    20: '>Lk 3:22',
    21: '>Lk 4:13',
    22: '>Lk 4:37',
    23: '>Lk 5:16',
    24: '>Lk 5:32',
    25: '>Lk 6:11',
    26: '>Lk 6:36',
    27: '>Lk 7:10',
    28: '>Lk 7:35',
    29: '>Lk 7:50',
    30: '>Lk 8:18',
    31: '>Lk 8:39',
}

psalms[MARCH] = {
    2: 'Ps 28',
    3: 'Ps 29',
    4: 'Ps 30',
    7: 'Ps 31',
    11: 'Ps 32',
    12: 'Ps 33',
    15: 'Ps 34',
    18: 'Ps 35',
    22: 'Ps 36',
    23: 'Ps 37',
    28: 'Ps 38',
    31: 'Ps 39',
}

proverbs[MARCH] = {
    1: 'Prov 6:12-19',
    5: 'Prov 6:20-29',
    9: 'Prov 6:30-35',
    13: 'Prov 7:1-5',
    17: 'Prov 7:6-20',
    21: 'Prov 7:21-27',
    25: 'Prov 8:1-11',
    29: 'Prov 8:12-21',
}

old_testament[APRIL] = {
    1: 'Num 31:25-32:42',
    2: '>Num 34:29',
    3: '>Num 36:13',
    4: 'Deut 1:1-2:23',
    5: '>Deut 4:14',
    6: '>Deut 5:33',
    7: '>Deut 8:20',
    8: '>Deut 10:22',
    9: '>Deut 12:32',
    10: '>Deut 14:29',
    11: '>Deut 16:20',
    12: '>Deut 18:22',
    13: '>Deut 20:20',
    14: '>Deut 22:30',
    15: '>Deut 25:19',
    16: '>Deut 28:14',
    17: '>Deut 28:68',
    18: '>Deut 30:10',
    19: '>Deut 31:29',
    20: '>Deut 32:52',
    21: '>Deut 34:12',
    22: 'Josh 1:1-2:24',
    23: '>Josh 5:12',
    24: '>Josh 7:26',
    25: '>Josh 9:15',
    26: '>Josh 10:43',
    27: '>Josh 12:24',
    28: '>Josh 14:15',
    29: '>Josh 16:10',
    30: '>Josh 18:28',
}

new_testament[APRIL] = {
    1: 'Lk 8:40-9:9',
    2: '>Lk 9:27',
    3: '>Lk 9:56',
    4: '>Lk 10:24',
    5: '>Lk 11:4',
    6: '>Lk 11:32',
    7: '>Lk 11:54',
    8: '>Lk 12:34',
    9: '>Lk 12:59',
    10: '>Lk 13:30',
    11: '>Lk 14:14',
    12: '>Lk 14:35',
    13: '>Lk 15:32',
    14: '>Lk 16:18',
    15: '>Lk 17:10',
    16: '>Lk 17:37',
    17: '>Lk 18:30',
    18: '>Lk 19:10',
    19: '>Lk 19:44',
    20: '>Lk 20:26',
    21: '>Lk 21:4',
    22: '>Lk 21:38',
    23: '>Lk 22:38',
    24: '>Lk 22:62',
    25: '>Lk 23:25',
    26: '>Lk 23:56',
    27: '>Lk 24:35',
    28: '>Lk 24:53',
    29: 'Jn 1:1-28',
    30: '>Jn 1:51',
}

psalms[APRIL] = {
    1: 'Ps 40',
    4: 'Ps 41',
    7: 'Ps 42',
    9: 'Ps 43',
    11: 'Ps 44',
    13: 'Ps 45',
    16: 'Ps 46',
    17: 'Ps 47',
    19: 'Ps 48',
    21: 'Ps 49',
    23: 'Ps 50',
    25: 'Ps 51',
    28: 'Ps 52',
    29: 'Ps 53',
}

proverbs[APRIL] = {
    2: 'Prov 8:22-31',
    6: 'Prov 8:36',
    10: 'Prov 9:1-12',
    14: 'Prov 9:13-18',
    18: 'Prov 10:1-10',
    22: 'Prov 10:11-20',
    26: 'Prov 10:21-30',
    30: 'Prov 10:31-11:8',
}

old_testament[MAY] = {
    1: 'Jos 19-21:19',
    2: '>Jos 22:34',
    3: '>Jos 24:33',
    4: '>Jdg 2:5',
    5: '>Jdg 3:31',
    6: '>Jdg 5:31',
    7: '>Jdg 7:8a',
    8: '>Jdg 8:35',
    9: '>Jdg 9:57',
    10: '>Jdg 11:40',
    11: '>Jdg 13:25',
    12: '>Jdg 15:20',
    13: '>Jdg 17:13',
    14: '>Jdg 19:30',
    15: '>Jdg 21:25',
    16: 'Ruth 1:1-2:23',
    17: '>Ruth 4:22',
    18: '1 Sam 1:1-2:26',
    19: '>1 Sam 4:22',
    20: '>1 Sam 7:17',
    21: '>1 Sam 10:8',
    22: '>1 Sam 12:25',
    23: '>1 Sam 14:23',
    24: '>1 Sam 15:35',
    25: '>1 Sam 17:37',
    26: '>1 Sam 18:30',
    27: '>1 Sam 20:42',
    28: '>1 Sam 23:29',
    29: '>1 Sam 25:44',
    30: '>1 Sam 28:25',
    31: '>1 Sam 31:13',
}

new_testament[MAY] = {
    1: 'Jn 2:1-25',
    2: '>Jn 3:21',
    3: '>Jn 3:36',
    4: '>Jn 4:26',
    5: '>Jn 4:42',
    6: '>Jn 5:15',
    7: '>Jn 5:30',
    8: '>Jn 5:47',
    9: '>Jn 6:24',
    10: '>Jn 6:59',
    11: '>Jn 7:13',
    12: '>Jn 7:44',
    13: '>Jn 8:11',
    14: '>Jn 8:30',
    15: 'Jn 8:31-59',
    16: '>Jn 9:34',
    17: '>Jn 10:21',
    18: '>Jn 10:42',
    19: '>Jn 11:44',
    20: '>Jn 12:11',
    21: '>Jn 12:36',
    22: '>Jn 13:17',
    23: '>Jn 13:38',
    24: '>Jn 14:31',
    25: '>Jn 16:4',
    26: '>Jn 17:5',
    27: '>Jn 17:26',
    28: '>Jn 18:24',
    29: '>Jn 18:40',
    30: '>Jn 19:27',
    31: '>Jn 20:9',
}

psalms[MAY] = {
    1: 'Ps 54',
    2: 'Ps 55',
    5: 'Ps 56',
    6: 'Ps 57',
    9: 'Ps 58',
    10: 'Ps 59',
    13: 'Ps 60',
    15: 'Ps 61',
    17: 'Ps 62',
    18: 'Ps 63',
    19: 'Ps 64',
    21: 'Ps 65',
    22: 'Ps 66',
    25: 'Ps 67',
    26: 'Ps 68',
}

proverbs[MAY] = {
    4: 'Prov 11:9-18',
    8: 'Prov 11:19-28',
    12: '>Prov 12:7',
    16: 'Prov 12:8-17',
    20: 'Prov 12:18-27',
    24: 'Prov 12:28-13:9',
    28: 'Prov 13:10-19',
}

old_testament[JUNE] = {
    1: '2 Sam 1:1-2:7',
    2: '> 2 Sam 3:21',
    3: '> 2 Sam 5:5',
    4: '> 2 Sam 6:23',
    5: '> 2 Sam 8:18',
    6: '> 2 Sam 10:19',
    7: '> 2 Sam 12:31',
    8: '> 2 Sam 13:39',
    9: '> 2 Sam 15:12',
    10: '> 2 Sam 16:14',
    11: '> 2 Sam 18:18',
    12: '> 2 Sam 19:43',
    13: '> 2 Sam 21:22',
    14: '> 2 Sam 23:7',
    15: '> 2 Sam 24:25',
    16: '1 Kings 1:1-2:12',
    17: '>1 Kings 3:15',
    18: '>1 Kings 5:18',
    19: '>1 Kings 7:22',
    20: '>1 Kings 8:21',
    21: '>1 Kings 9:9',
    22: '>1 Kings 11:13',
    23: '>1 Kings 12:24',
    24: '>1 Kings 14:20',
    25: '>1 Kings 16:7',
    26: '>1 Kings 18:15',
    27: '>1 Kings 19:21',
    28: '>1 Kings 21:29',
    29: '>1 Kings 22:53',
    30: '2 Kings 1:1-2:25',
}

new_testament[JUNE] = {
    1: 'Jn 20:10-31',
    2: '>Jn 21:25',
    3: 'Acts 1:1-22',
    4: '>Acts 2:21',
    5: '>Acts 2:47',
    6: '>Acts 3:26',
    7: '>Acts 4:22',
    8: '>Acts 5:11',
    9: '>Acts 5:42',
    10: '>Acts 7:19',
    11: '>Acts 7:43',
    12: '>Acts 8:3',
    13: '>Acts 8:40',
    14: '>Acts 9:31',
    15: '>Acts 10:23a',
    16: '>Acts 11:18',
    17: '>Acts 12:19a',
    18: '>Acts 13:12',
    19: '>Acts 13:41',
    20: '>Acts 14:7',
    21: '>Acts 14:28',
    22: '>Acts 15:21',
    23: '>Acts 15:41',
    24: '>Acts 16:15',
    25: '>Acts 16:40',
    26: '>Acts 17:21',
    27: '>Acts 18:8',
    28: '>Acts 19:13',
    29: '>Acts 19:41',
    30: '>Acts 20:38',
}

psalms[JUNE] = {
    2: 'Ps 69',
    6: 'Ps 70',
    7: 'Ps 71',
    11: 'Ps 72',
    12: 'Ps 73',
    15: 'Ps 74',
    19: 'Ps 75',
    20: 'Ps 76',
    22: 'Ps 77',
    24: 'Ps 78',
}

proverbs[JUNE] = {
    1: 'Prov 13:20-14:4',
    5: 'Prov 14:5-14',
    9: 'Prov 14:15-24',
    13: 'Prov 14:25-35',
    17: 'Prov 15:1-10',
    21: 'Prov 15:11-20',
    25: 'Prov 15:21-30',
    29: '>Prov 16:7',
}


def _split_reference(reference):
    return reference.rsplit(' ', 1)


def _end_ref_from_reading(reading):
    """Get the last reference from the reading text
    Example: if reading text is 'John 1:1-3:16', this function will return
    'John 3:16'
    >>> _end_ref_from_reading('John 1:1-3:16')
    'John 3:16'
    >>> _end_ref_from_reading('John 1:1-2')
    'John 1:2'
    >>> _end_ref_from_reading('John 8:31-59')
    'John 8:59'
    """
    if reading.startswith('>'):
        return reading[1:].strip()
    if '-' in reading:
        first_ref, second_ref = reading.split('-', 1)
        book, remainder = _split_reference(first_ref)
        if ":" in remainder and ":" not in second_ref:
            second_ref = "{}:{}".format(
                remainder.split(":")[0], second_ref.strip())
        return '{} {}'.format(book.strip(), second_ref.strip())
    return reading


def _strip_book(reference):
    """Strip the book name from the reference
    Example: If reference is 'John 3:16', this function will return '3:16'
    >>> _strip_book('John 3:16')
    '3:16'
    >>> _strip_book('Jn 8:31-59')
    '8:31-59'
    >>> _strip_book('>1 Sam 7:17')
    '7:17'
    """
    return _split_reference(reference)[1]


def _get_reading(dic, day):
    """Format the reading using the last reading, if necessary"""
    orig_reading = reading = dic[day]
    if '__last__' in dic:
        last = dic['__last__']
        if reading.startswith('>'):
            reading = '{}-{}'.format(_end_ref_from_reading(last),
                                     _strip_book(reading[1:].strip()))
    dic['__last__'] = orig_reading
    return reading


def _format_readings(month):
    data = {}
    for day in xrange(1, len(old_testament[month]) + 1):
        reading = [_get_reading(old_testament[month], day),
                   _get_reading(new_testament[month], day)]
        if day in psalms[month]:
            reading.append(_get_reading(psalms[month], day))
        if day in proverbs[month]:
            reading.append(_get_reading(proverbs[month], day))
        data[day] = tuple(reading)
    return data


readings = {
    JANUARY: _format_readings(JANUARY),
    FEBRUARY: _format_readings(FEBRUARY),
    MARCH: _format_readings(MARCH),
    APRIL: _format_readings(APRIL),
    MAY: _format_readings(MAY),
    JUNE: _format_readings(JUNE),
}

if __name__ == "__main__":
    from pprint import pprint
    try:
        month = int(sys.argv[1])
    except (IndexError, ValueError):
        month = None
    if month and month in readings:
        pprint(readings[month])
    else:
        pprint(readings)
