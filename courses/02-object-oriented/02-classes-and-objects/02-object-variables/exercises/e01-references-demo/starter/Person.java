// Person is done for you. Don't change it.
// The Person(...) part is a constructor: it lets you give a person a name and age
// right when you make it. We'll write our own constructors in a couple of lessons.
public class Person {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    String getName() {
        return name;
    }

    void setName(String newName) {
        name = newName;
    }

    int getAge() {
        return age;
    }
}
