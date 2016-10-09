#include <QLabel>
#include <QVBoxLayout>
#include <QApplication>
#include <QPushButton>
#include <QVector>

int pierwszyProgram(int argc, char *argv[]) {
    QApplication app(argc, argv);
    QLabel label("Hello world!");
    label.setAlignment(Qt::AlignCenter);
    label.setFixedSize(200,50);
    label.show();
    return app.exec();
}

int drugiProgram(int argc, char *argv[]) {
    QApplication app(argc, argv);
    QWidget window;
    QVBoxLayout* mainLayout = new QVBoxLayout(&window);
    QLabel* label1 = new QLabel("One");
    QLabel* label2 = new QLabel("Two");
    mainLayout->addWidget(label1);
    mainLayout->addWidget(label2);
    window.show();
    return app.exec();
}

int trzeciProgram(int argc, char *argv[]) {
    QApplication app(argc, argv);
    QWidget window;
    QHBoxLayout* mainLayout = new QHBoxLayout(&window);
    mainLayout->addWidget(new QLabel("One"));
    mainLayout->addWidget(new QLabel("Two"));
    window.show();
    return app.exec();
}

int czwartyProgram(int argc, char *argv[]) {
    QApplication app(argc, argv);
    QWidget window;
    QGridLayout* mainLayout = new QGridLayout(&window);
    mainLayout->addWidget(new QLabel("One"), 0, 0);
    mainLayout->addWidget(new QLabel("Two"), 0, 1);
    mainLayout->addWidget(new QLabel("Three"), 1, 0);
    mainLayout->addWidget(new QLabel("Four"), 1, 1);
    mainLayout->addWidget(new QLabel("Five"), 2, 0);
    mainLayout->addWidget(new QLabel("Six"), 2, 1);
    window.show();
    return app.exec();
}

int piatyProgram(int argc, char *argv[]) {
    QApplication app(argc, argv);
    QWidget window;
    QPushButton *quit = new QPushButton("Close all",&window);
    QObject::connect(quit,&QPushButton::clicked, &window, &QWidget::close);
    window.show();
    return app.exec();
}

int main(int argc, char *argv[]) {
    pierwszyProgram(argc, argv);
    drugiProgram(argc, argv);
    trzeciProgram(argc, argv);
    czwartyProgram(argc, argv);
    piatyProgram(argc, argv);
    return 0;
}
