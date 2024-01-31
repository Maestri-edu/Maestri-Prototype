import { StyleSheet } from "react-native";
import colors from "../../design-System/global-styles";

const styles = StyleSheet.create({

    iconBox:{
        alignItems:"center",
    },
    
    icon:{
        width: 40,
        height: 40,
        backgroundColor:colors.lightBlue,
        borderRadius:30,
        textAlign:"center",
        textAlignVertical:"center",
        color:colors.midnightBlue,

    },

    iconLabel:{
        fontSize:12
    }
})

export default styles;
