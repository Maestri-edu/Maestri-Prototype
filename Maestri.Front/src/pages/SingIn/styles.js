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
  button: {
    width: "70%",
    height: 50,
    backgroundColor: colors.darkBlue,
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    borderRadius: 20,
    opacity: 0.8,
    marginVertical: 20,
  },
  buttonText: {
    color: colors.softWhite,
    fontSize: 20,
    fontWeight: "bold",
  },
});

export default styles;
