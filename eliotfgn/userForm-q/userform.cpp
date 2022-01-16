#include "userform.h"
#include "ui_userform.h"
#include <QMessageBox>


UserForm::UserForm(QWidget *parent): QDialog(parent), ui(new Ui::UserForm)
{
    ui->setupUi(this);

    l_firstname = new QLabel("Firstname :", this);
    le_firstname = new QLineEdit(this);
    le_firstname->move(120, 0);

    l_lastname = new QLabel("Lastname :", this);
    l_lastname->move(0, 40);
    le_lastname = new QLineEdit(this);
    le_lastname->move(120, 40);

    btn_save = new QPushButton("Save", this);
    btn_save->move(0, 80);
    connect(btn_save, SIGNAL(clicked()), this, SLOT(saveUser()));
}

UserForm::~UserForm()
{
    delete ui;
}

void UserForm::saveUser() {
    if (!le_lastname->text().isEmpty() && !le_firstname->text().isEmpty()) {
        users.push_back(User(le_lastname->text(), le_firstname->text()));
    }
    else {
        QMessageBox::critical(this, "Saving", "User registered");
    }
}
