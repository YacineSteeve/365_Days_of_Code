#ifndef USER_H
#define USER_H
#include <QString>


class User
{
private:
    QString firstname, lastname;
public:
    User();
    User(QString fname, QString lname);
    QString getFirstname();
    QString getLastname();
    void setLastname(QString);
    void setFirstname(QString);

};

#endif // USER_H
