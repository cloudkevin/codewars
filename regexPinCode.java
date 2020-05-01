// ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
// If the function is passed a valid PIN string, return true, else return false.

public static boolean validatePin(String pin) {
		int len = pin.length();
		if (pin.startsWith("+") || pin.startsWith("-")) {
			return false;
		}
		if (len == 4 || len == 6) {
			try {
				int parsed = Integer.parseInt(pin);
				if (parsed < 0) {
					return false;
				}
				return true;
			}
			catch (NumberFormatException e){
				return false;
			}
		}
		return false;
	}