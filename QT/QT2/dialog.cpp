#include "dialog.h"
#include <QDebug>
Dialog::Dialog(QWidget *parent)
    : QDialog(parent), btcvr(parent) {
    layout = new QVBoxLayout(this);
    layout->addLayout(composeTop());
    layout->addItem(new QSpacerItem(0,20));
    layout->addLayout(addButton());
    connections();
}


QGridLayout* Dialog::composeTop() {
    QGridLayout *layout = new QGridLayout;
    layout->addWidget(label("Bin"), 0, 0);
    layout->addWidget(label("Hex"), 1, 0);
    layout->addWidget(label("Dec"), 2, 0);
    layout->addWidget(textBox(),0,1);
    layout->addWidget(textBox(),1,1);
    layout->addWidget(textBox(),2,1);
    return layout;
}

QHBoxLayout* Dialog::addButton() {
    QHBoxLayout *layout;
    pushButton = new QPushButton("Quit",this);
    layout = new QHBoxLayout;
    layout->addItem(new QSpacerItem(80,0));
    layout->addWidget(pushButton);
    return layout;
}

void Dialog::connections() {
    connect(pushButton, &QPushButton::clicked, this, &Dialog::close);
    connect(textBoxes[0], &QLineEdit::textEdited, &btcvr, &ByteConverter::setBin);
    connect(textBoxes[1], &QLineEdit::textEdited, &btcvr, &ByteConverter::setHex);
    connect(textBoxes[2], &QLineEdit::textEdited, &btcvr, &ByteConverter::setDec);
    connect(&btcvr, &ByteConverter::decChanged, textBoxes[2], &QLineEdit::setText);
    connect(&btcvr, &ByteConverter::hexChanged, textBoxes[1], &QLineEdit::setText);
    connect(&btcvr, &ByteConverter::binChanged, textBoxes[0], &QLineEdit::setText);
}

QLabel* Dialog::label(const QString &str) {
    labels.push_back(new QLabel(str,this));
    return labels[labels.size()-1];
}

QLineEdit* Dialog::textBox() {
    textBoxes.push_back(new QLineEdit);
    return textBoxes[textBoxes.size()-1];
}

void ByteConverter::setBin(const QString &str) {
    QString first(binToDec(str));
    QString second(binToHex(str));
    decChanged(first);
    hexChanged(second);
}

void ByteConverter::setHex(const QString &str) {
    QString first(hexToBin(str));
    QString second(hexToDec(str));
    binChanged(first);
    decChanged(second);
}

void ByteConverter::setDec(const QString &str) {
    QString first(decToBin(str));
    QString second(decToHex(str));
    binChanged(first);
    hexChanged(second);
}

inline char QCharToChar(QChar character) {
    for(char a = '0'; a <= '9'; a++)
        if(a == character)
            return a;
    for(char a = 'a'; a <= 'f'; a++)
        if(a == character)
            return a;
    return '0';
}

int ByteConverter::fromBin(const QString &bin) {
    int ans = 0;
    for(auto it = bin.begin(); it != bin.end(); it++) {
        ans *= 2;
        ans += QCharToChar(*it) - '0';
    }
    return ans;
}

int ByteConverter::fromHex(const QString &hex) {
    int ans = 0;
    for(auto it = hex.begin(); it != hex.end(); it++) {
        ans *= 16;
        ans += [](char a)->int {
            if(a <= '9')
                return a - '0';
            else
                return a - 'a' + 10;
        }(QCharToChar(*it));
    }
    return ans;
}

int ByteConverter::fromDec(const QString &dec) {
    int ans = 0;
    for(auto it = dec.begin(); it != dec.end(); it++) {
        ans *= 10;
        ans += QCharToChar(*it) - '0';
    }
    return ans;
}

QString ByteConverter::toBin(int bin) {
    QString temp, ans;
    while(bin) {
        temp += static_cast<char>(bin % 2) + '0';
        bin /= 2;
    }
    for(int i = static_cast<int>(temp.size() - 1); i >= 0; i--)
        ans += temp[i];
    return ans;
}

QString ByteConverter::toHex(int hex) {
    QString temp, ans;
    while(hex) {
        temp += hex % 16 < 10 ? static_cast<char>(hex % 16) + '0' : static_cast<char>(hex % 16) + 'a' - 10;
        hex /= 16;
    }
    for(int i = static_cast<int>(temp.size() - 1); i >= 0; i--)
        ans += temp[i];
    return ans;
}

QString ByteConverter::toDec(int dec) {
    QString temp, ans;
    while(dec) {
        temp += static_cast<char>(dec % 10) + '0';
        dec /= 10;
    }
    for(int i = static_cast<int>(temp.size() - 1); i >= 0; i--)
        ans += temp[i];
    return ans;
}
