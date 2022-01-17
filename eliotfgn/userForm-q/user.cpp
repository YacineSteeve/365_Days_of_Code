#include "user.h"

using namespace std;

User::User() {}

User::User(QString fname, QString lname) {
    lastname = lname;
    firstname = fname;
}

QString User::getLastname() {
    return lastname;
}

QString User::getFirstname() {
    return firstname;
}

void User::setLastname(QString _lastname) {
    lastname = _lastname;
}

void User::setFirstname(QString _firstname) {
    firstname = _firstname;
}

