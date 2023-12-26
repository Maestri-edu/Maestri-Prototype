import { StyleSheet } from "react-native";
import colors from "../../../design-System/global-styles";

const styles = StyleSheet.create({
    container: {
        flex: 1,
        position: "relative",
      },
    
      contentBox: {
        flex: 1,
        width: "100%",
        height: "100%",
        display: "flex",
        position: "absolute",
        justifyContent: "center",
        alignItems: "center",
      },
    
      title: {
        fontSize: 20,
        color: colors.softWhite,
        marginBottom: 20,
      },
    
      button: {
        width: 500,
        height:60,
        borderRadius:40
      },
})

export default styles;