#ifndef USERFORM_H
#define USERFORM_H

#include <QDialog>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>

QT_BEGIN_NAMESPACE
namespace Ui { class UserForm; }
QT_END_NAMESPACE

class UserForm : public QDialog
{
    Q_OBJECT

public:
    UserForm(QWidget *parent = nullptr);
    ~UserForm();

private:
    Ui::UserForm *ui;
    QLabel *l_lastname, *l_firstname;
    QLineEdit *le_lastname, *le_firstname;
    QPushButton *btn_save;

private slots:
    void saveUser();
};
#endif // USERFORM_H
