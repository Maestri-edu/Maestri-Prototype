import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  image: {
    flex: 1,
    width: "100%",
    height: "100%",
    resizeMode: "cover",
    position: "absolute",
  },

  gradient: {
    position:"absolute",
    left:0,
    right:0,
    top:"75%",
    height:"25%",
    transform:[{ scaleY: -1 }]
  },
  mask: {
    ...StyleSheet.absoluteFillObject,
    backgroundColor: "rgba(0, 0, 0, 0.5)", // Cor e opacidade da máscara
  },
});

export default styles;
