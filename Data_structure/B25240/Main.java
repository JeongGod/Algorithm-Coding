package B25240;

import java.io.*;
import java.util.*;

class Filejo {
    int ownerPer, groupPer, otherPer;
    String owner, group;

    public Filejo(int ownerPer, int groupPer, int otherPer, String owner, String group) {
        this.ownerPer = ownerPer;
        this.groupPer = groupPer;
        this.otherPer = otherPer;
        this.owner = owner;
        this.group = group;
    }

    public boolean checkPermission(int status, char command) {
        int operation;
        if (command == 'R') operation = 4;
        else if (command == 'W') operation = 2;
        else operation = 1;
        switch (status) {
            case 0:
                return (otherPer & operation) > 0;
            case 1:
                return ((groupPer | otherPer) & operation) > 0;
            case 2:
                return ((ownerPer | groupPer | otherPer) & operation) > 0;
            default:
                return false;
        }
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()), f = Integer.parseInt(st.nextToken());
        HashMap<String, Set<String>> users = new HashMap<>();
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            String user = st.nextToken();
            Set<String> userGroups = users.getOrDefault(user, new HashSet<>());
            userGroups.add(user);
            if (st.hasMoreTokens()) {
                String[] groups = st.nextToken().split(",");
                userGroups.addAll(Arrays.asList(groups));
            }
            users.put(user, userGroups);
        }

        HashMap<String, Filejo> files = new HashMap<>();
        for (int i=0; i<f; i++) {
            st = new StringTokenizer(br.readLine());
            String filename = st.nextToken();
            String permission = st.nextToken();
            String owner = st.nextToken();
            String oGroup = st.nextToken();
            files.put(filename, new Filejo(permission.charAt(0) - '0', permission.charAt(1) - '0', permission.charAt(2) - '0', owner, oGroup));
        }

        int q = Integer.parseInt(br.readLine());
        for (int i=0; i<q; i++) {
            st = new StringTokenizer(br.readLine());
            String user = st.nextToken();
            String filename = st.nextToken();
            String operation = st.nextToken();

            Filejo file = files.get(filename);
            boolean result;
            if (file.owner.equals(user)) {
                result = file.checkPermission(2, operation.charAt(0));
            } else if (users.get(user).contains(file.group)) {
                result = file.checkPermission(1, operation.charAt(0));
            } else {
                result = file.checkPermission(0, operation.charAt(0));
            }
            System.out.println(result ? 1 : 0);
        }
    }
}

