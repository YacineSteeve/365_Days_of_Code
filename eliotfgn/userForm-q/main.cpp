#include "userform.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    UserForm w;
    w.show();
    return a.exec();
}
