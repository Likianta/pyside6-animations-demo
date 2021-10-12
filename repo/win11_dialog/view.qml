import QtQuick
import QtQuick.Window

Window {
    width: 900
    height: 540
    color: '#AFAFAF'
    visible: true

    Rectangle {
        anchors.centerIn: parent
        width: 550
        height: 250
        border.width: 0
        radius: 8
        color: '#FFFFFF'

        Rectangle {
            id: bottom_stripe
            anchors.bottom: parent.bottom
            width: parent.width
            height: 100
            color: '#F3F3F3'
            radius: 8

            Rectangle {
                id: corner_fills
                anchors.top: parent.top
                width: parent.width
                height: parent.radius
                color: parent.color
                radius: 0
            }

            Rectangle {
                id: primary_btn
                anchors.left: parent.left
                anchors.leftMargin: 15
                anchors.verticalCenter: parent.verticalCenter
                color: '#005FBB'
                radius: bottom_stripe.radius
                height: 40

                Text {
                    anchors.centerIn: parent
                    color: 'white'
                    text: 'Text'
                }
            }

            Rectangle {
                id: secondary_btn
                anchors.right: parent.right
                anchors.rightMargin: 15
                anchors.verticalCenter: parent.verticalCenter
                // border.width: 1
                color: '#FBFBFB'
                radius: bottom_stripe.radius
                height: 40

                Text {
                    anchors.centerIn: parent
                    color: 'black'
                    text: 'Text'
                }
            }

            Component.onCompleted: {
                function decide_button_width() {
                    let side_padding = 15
                    let mid_padding = 10
                    let result = (bottom_stripe.width - side_padding * 2 - mid_padding) / 2
                    return result
                }

                primary_btn.width = decide_button_width()
                secondary_btn.width = decide_button_width()
            }
        }
    }
}
