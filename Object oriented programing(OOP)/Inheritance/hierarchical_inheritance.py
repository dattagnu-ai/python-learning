# quirements:

# Employee मध्ये work() method असावा.
# Developer मध्ये code() method असावा.
# Manager मध्ये manage() method असावा.
# Developer आणि Manager दोघांनी Employee inherit करावा.
# दोन्हीचे objects तयार कर.
# प्रत्येक object मधून त्याचा स्वतःचा method आणि inherited work() call कर.


class Employee:
    def Work(self):
        print("i am working")


class Developer(Employee):
    def code(self):
        print("on learning code")


class Manager(Employee):
    def manage(self):
        print("Im a manager")


dev = Developer()
dev.code()
dev.Work()

man = Manager()
man.Work()
man.manage()
