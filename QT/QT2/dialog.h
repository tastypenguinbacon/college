#ifndef DIALOG_H
#define DIALOG_H

#include <QDialog>
#include <QObject>
#include <QGridLayout>
#include <QLabel>
#include <QPushButton>
#include <QSpacerItem>
#include <QLineEdit>

class ByteConverter : public QObject {
    Q_OBJECT
    int fromBin(const QString &bin);
    int fromHex(const QString &hex);
    int fromDec(const QString &dec);
    QString toBin(int bin);
    QString toHex(int hex);
    QString toDec(int dec);
public:
    ByteConverter(QObject* = 0) {}
    QString binToDec(const QString &bin) {return bin.size() > 0 ? toDec(fromBin(bin)) : "";}
    QString decToBin(const QString &dec) {return dec.size() > 0 ? toBin(fromDec(dec)) : "";}
    QString binToHex(const QString &bin) {return bin.size() > 0 ? toHex(fromBin(bin)) : "";}
    QString hexToBin(const QString &hex) {return hex.size() > 0 ? toBin(fromHex(hex)) : "";}
    QString hexToDec(const QString &hex) {return hex.size() > 0 ? toDec(fromHex(hex)) : "";}
    QString decToHex(const QString &dec) {return dec.size() > 0 ? toHex(fromDec(dec)) : "";}
public slots:
    void setDec(const QString&);
    void setHex(const QString&);
    void setBin(const QString&);
signals:
    void decChanged(const QString&);
    void hexChanged(const QString&);
    void binChanged(const QString&);
};


class Dialog : public QDialog {
    Q_OBJECT
public:
    Dialog(QWidget *parent = 0);
    ~Dialog() {}
private:
    QVector<QLabel*> labels;
    QVector<QLineEdit*> textBoxes;
    QPushButton *pushButton;
    QVBoxLayout *layout;

    QLabel* label(const QString& str);
    QLineEdit* textBox();
    QGridLayout *composeTop();
    QHBoxLayout *addButton();
    void connections();
    ByteConverter btcvr;
};

#endif // DIALOG_H
