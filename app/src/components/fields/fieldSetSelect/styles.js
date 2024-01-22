import { StyleSheet } from "react-native";
import colors from "../../../design-System/global-styles";

const styles = StyleSheet.create({
    label: {
        fontSize: 20,
        fontWeight: "500",
        color: colors.softWhite,
        alignSelf: "flex-start",
        marginStart: 30,
        marginTop: 5
    },

    placeholder: {
        color: colors.mediumGray,
    },
    input:{
        borderWidth:0,
        borderBottomWidth:2,
        borderColor:colors.softWhite,
        width: "80%",
        height: 30,
        color:colors.mediumGray
    },

    boxArea: {
        width: "80%",
        borderColor: "white",
        borderWidth: 1,
        padding: 5,
        borderRadius: 5,
        borderBottomLeftRadius:0,
        marginVertical:5
    },

    invalidFeedBack: {
        color: colors.accentRed,
        fontSize: 12,
        alignSelf: "flex-start",
        marginStart: 32
    },

    fieldSet: {
        width: "100%",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
    },

    selectList: {
        width: "auto",
        borderColor: "white",
        borderWidth: 1,
        // padding: 5,
        marginEnd: "auto",
        marginLeft: 36,
        borderTopLeftRadius: 0,
        borderTopRightRadius: 0,
        borderBottomLeftRadius: 5,
        borderBottomRightRadius: 5,
    },

    itemList: {
        width: "100%",
        color: "white",
        fontWeight: "bold",
        padding: 5,
        borderBottomWidth: 1,
        borderColor: "gray"
    }
})

export default styles