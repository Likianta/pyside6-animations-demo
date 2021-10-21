import QtQuick
import QtQuick.Controls
import LightClean

LCWindow {
    id: root

    Flickable {
//        anchors.fill: parent
        width: root.width
        height: root.height
        contentWidth: flow.width
        contentHeight: flow.height

        Flow {
            id: flow
            width: root.width
            height: childrenRect.height + 100
            spacing: 1
            //  tip: use mini spacing but large clickable area for better
            //       experience. see also `id:area`

            Repeater {
                delegate: Item {
                    width: 250
                    height: 150
//                    height: index % 2 == 0 ? 150 : 200

                    Image {
                        source: modelData

                        LCRectangle {
                            id: img_mask
                            anchors.fill: parent
                            opacity: img_mask.p_selected ? 0.5 : 0.0
                            p_color: '#000000'

                            property bool p_selected: false

                            Behavior on opacity {
                                NumberAnimation {
                                    duration: 80
                                }
                            }

                            Component.onCompleted: {
                                area.clicked.connect(() => {
                                    img_mask.p_selected = !img_mask.p_selected
                                })
                            }
                        }

                        LCRectangle {
                            anchors.centerIn: parent
                            width: parent.width + 6
                            height: parent.height + 6
                            border.width: area.p_hovered ? 2 : 0
                            border.color: '#0E549C'
                            p_color: 'transparent'
                        }

                        LCIcon {
                            visible: img_mask.p_selected
                            p_size: 17
                            p_source: 'check_circle.svg'
                            Component.onCompleted: {
                                LKLayoutHelper.quick_anchors(this, parent, {
                                    'reclines': [0, 0, 1, 1],
                                    'margins': [0, 0, 6, 3]
                                })
                            }
                        }

                        Component.onCompleted: {
                            LKLayoutHelper.quick_anchors(this, parent, {
                                'reclines': 'fill',
                                'margins': [12, 4, 12, 4]
                            })
                        }
                    }

                    LCMouseArea {
                        id: area
                        anchors.fill: parent
                        p_hover_enabled: true
                    }
                }

                Component.onCompleted: {
                    this.model = pyside.eval(`
                        import os

                        # test 1: use my local existed dir
                        # dir_i = 'E:/pictures/temp'
                        dir_i = input("gallery folder: ")

                        filenames = os.listdir(dir_i)
                        print('find {} pictures in this folder'.format(
                            len(filenames))
                        )

                        # test 2: test long gallery
                        return [f'file:///{dir_i}/{x}' for x in filenames] * 40
                        # return [f'file:///{dir_i}/{x}' for x in filenames]
                    `)
                }
            }
        }
    }
}
