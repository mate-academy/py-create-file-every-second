from datetime import datetime
import time


def main():
    while True:
        st_1 = str(datetime.now())
        st = st_1.split()
        st = st[1]
        st = st.split(".")
        st = st[0]
        st = st.split(":")
        st_r = f"app-{st[0]}_{st[1]}_{st[2]}.log"
        st_0 = st_1.split(".")
        st_0 = st_0[0]
        with open(st_r, "w") as f:
            f.write(st_1)
        print(f"{st_0} {st_r}")
        time.sleep(1)


if __name__ == "__main__":
    main()
