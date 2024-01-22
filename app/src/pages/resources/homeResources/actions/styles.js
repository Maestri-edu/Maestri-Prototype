import { StyleSheet } from "react-native";
import colors from "../../../../design-System/global-styles";

const styles = StyleSheet.create({
    actionsBox:{
        width:"100%",
        height: 80,
        backgroundColor:colors.softWhite,
        borderTopStartRadius:30,
        borderTopEndRadius:30,
        marginTop:-10,
        padding:10,
        flexDirection:"row",
        justifyContent:"space-around"

    }
})

export default styles