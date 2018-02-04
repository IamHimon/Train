from datetime import datetime


def readData(data_file, station):
    file_reader = open(data_file, encoding='utf-8')
    with file_reader as reader:
        records = []
        data_lines = reader.readlines()
        for record in data_lines:
            R = record.strip().split()
            if len(R) != 4:
                raise Exception("This line of Record is error!")
            records.append((R[0], datetime.strptime(R[1], '%H:%M'), [station for station in R[2].split(',')],
                            datetime.strptime(R[3], '%H:%M')))

    def judge(x: str, stations: list):
        for s in stations:
            if (x == s) or (x in s) or (s in x):
                return True
        return False

    result = list(filter(lambda x: judge(station, x[2]), records))

    print("从 徐州->上海，途径 [%s] 的班次(高铁/动车)有:" % station)
    for r in result:
        print(r[0], r[1])


if __name__ == '__main__':
    readData('data/new.txt', '无锡')

