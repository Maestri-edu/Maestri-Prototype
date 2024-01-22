import { StyleSheet } from "react-native";
import colors from "../../../../design-System/global-styles";

const styles = StyleSheet.create({
    informationBox: {
        width: "95%",
        height: "45%",
        backgroundColor: "black",
        marginStart:"2.5%",
        padding: 20,
        marginTop: 30,
        borderTopLeftRadius: 30,   // Raio dos cantos superior esquerdo
        borderTopRightRadius: 30,  // Raio dos cantos superior direito
    },

    textInformation: {
        color: colors.softWhite,
        fontSize: 20,
    },

    TitleInformation: {
        color: colors.lightBlue,
        fontSize: 40,
        fontWeight: "100"
    },

    userIcon: {
        color: colors.lightBlue,
        width: 50,
        height: 50,
        backgroundColor: "gray",
        textAlign: "center",
        textAlignVertical: "center",
        fontSize: 20,
        fontWeight: "900",
        borderRadius: 50
    },

    boxSaldo: {
        width: "100%",
        height: 100,
        backgroundColor: colors.darkGray,
        marginTop: 20,
        borderTopEndRadius: 10,
        borderTopStartRadius: 10,
        padding: 10,
    },

    textSaldo:{
        color: colors.softWhite,
        fontSize: 17,
        fontWeight:"200"
    },

    saldo: {
        fontSize: 25,
        color: colors.mediumGray,
        fontWeight: "900",
        textShadowColor: 'black',
        marginTop:10
    },

    iconButton:{
        position:"relative",
        marginLeft:"90%",
        marginTop:"-10%",
        backgroundColor:colors.midnightBlue,
        alignItems:"center",
        justifyContent:"center",
        width:30,
        height: 30,
        borderRadius:50
    },

    icon:{
        color:colors.softWhite
    },
    BoxAfterSaldo:{
        width:"100%",
        height: 40,
        backgroundColor:colors.mediumGray,
        borderBottomStartRadius:10,
        borderBottomEndRadius:10,
        paddingHorizontal:10,
        flexDirection:"row",
        justifyContent:"space-between",
        alignItems:"center"
    },
    textAfterSaldo:{
        color:colors.softWhite,
        fontSize:18,
        fontFamily:"monospace",
    }
})

export default styles