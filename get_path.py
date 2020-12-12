from ros import find_node, get_package_dir

package_name=
path=get_package_dir(package_name)

if __name__ == "__main__":
    print(path)