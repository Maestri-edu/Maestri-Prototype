import { StyleSheet } from "react-native";
import colors from "../../../../design-System/global-styles";

const styles = StyleSheet.create({
  iconMaestri: {
    width: 50,
    height: 50,
    marginBottom: 10,
    backgroundColor: colors.midnightBlue,
    borderRadius: 50,
    justifyContent: "center",
    alignItems: "center",
    shadowColor: "#000", // Cor da sombra
    shadowOffset: { width: 1, height: 4 },
    shadowOpacity: 0.7, // Opacidade da sombra
    shadowRadius: 4,
    elevation: 8, // Adiciona sombra no Android
  },
});

export default styles;
